import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import re
import json
import os
import markdown
from pathlib import Path

# Basic rate limiting to be polite to the server
REQUEST_DELAY = 0.5  # seconds

# URL list file path
DOCS_URL_FILE = "docs_url.txt"

def is_valid_url(url, base_domain):
    """Checks if a URL is valid and belongs to the target domain."""
    parsed_url = urlparse(url)
    # Ensure it's http/https and has the base domain in the netloc
    return (parsed_url.scheme in ['http', 'https'] and
            base_domain in parsed_url.netloc and
            not parsed_url.fragment)  # Ignore fragment links on the same page

def get_page_content(url):
    """Fetches the HTML content of a given URL."""
    try:
        headers = {'User-Agent': 'MCPServerGeneratorCrawler/1.0'}  # Identify our crawler
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        # Ensure content type is HTML before proceeding
        if 'text/html' in response.headers.get('Content-Type', ''):
            return response.text
        else:
            print(f"Skipping non-HTML content at {url} (Content-Type: {response.headers.get('Content-Type')})")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error fetching {url}: {e}")
        return None

def extract_links(html_content, base_url):
    """Extracts all valid internal links from HTML content."""
    links = set()
    soup = BeautifulSoup(html_content, 'html.parser')
    base_domain = urlparse(base_url).netloc

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Construct absolute URL
        absolute_url = urljoin(base_url, href)
        # Clean URL (remove query params, fragments for uniqueness check)
        cleaned_url = urlparse(absolute_url)._replace(query='', fragment='').geturl()

        if is_valid_url(cleaned_url, base_domain):
            links.add(cleaned_url)
    return links

def extract_code_blocks(soup):
    """Extract code blocks with their language information."""
    code_blocks = []
    
    # Find all code blocks (pre and code tags)
    for pre_tag in soup.find_all('pre'):
        code_tag = pre_tag.find('code')
        if code_tag:
            # Try to determine the language from class attributes
            language = "text"  # Default
            for class_name in code_tag.get('class', []):
                if class_name.startswith('language-'):
                    language = class_name.replace('language-', '')
                    break
            
            code_content = code_tag.get_text()
            code_blocks.append({
                'language': language,
                'content': code_content
            })
    
    return code_blocks

def extract_content_with_code(html_content, url):
    """Extracts meaningful text content and code blocks from HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # --- Attempt to remove common boilerplate elements ---
    selectors_to_remove = [
        'header', 'footer', 'nav', '.navbar', '.sidebar', '.toc',
        'script', 'style', 'aside', '.breadcrumb', '#breadcrumbs',
        '.edit-page-link', '.page-meta', '.feedback-widget'
    ]
    for selector in selectors_to_remove:
        for element in soup.select(selector):
            element.decompose()  # Remove the element and its content

    # --- Extract code blocks first ---
    code_blocks = extract_code_blocks(soup)
    
    # --- Extract text from the remaining main content area ---
    main_content = soup.find('main') or soup.find('article') or soup.find('div', role='main') or soup.body
    if not main_content:
        main_content = soup  # Fallback to the whole soup if no main element found

    # Get text, strip leading/trailing whitespace, and handle multiple lines
    text_lines = [line.strip() for line in main_content.get_text(separator='\n', strip=True).splitlines()]
    # Remove empty lines and potentially excessive whitespace lines
    meaningful_text = "\n".join(line for line in text_lines if line and not re.match(r"^\s*$", line))

    # Basic cleaning: replace multiple spaces/newlines
    meaningful_text = re.sub(r'\s{2,}', ' ', meaningful_text)
    meaningful_text = re.sub(r'\n{3,}', '\n\n', meaningful_text)

    if not meaningful_text.strip() and not code_blocks:
        print(f"Warning: No meaningful content extracted from {url}")
        return None

    # Get the page title
    title = soup.title.string if soup.title else urlparse(url).path.split('/')[-1]
    
    return {
        'title': title.strip(),
        'text': meaningful_text.strip(),
        'code_blocks': code_blocks,
        'url': url
    }

def convert_to_markdown(content):
    """Convert the extracted content to markdown format."""
    if not content:
        return None
        
    markdown_content = f"# {content['title']}\n\n"
    markdown_content += f"Source: [{content['url']}]({content['url']})\n\n"
    markdown_content += content['text'] + "\n\n"
    
    # Add code blocks with proper markdown formatting
    if content['code_blocks']:
        markdown_content += "## Code Examples\n\n"
        for i, block in enumerate(content['code_blocks']):
            markdown_content += f"### Code Example {i+1} ({block['language']})\n\n"
            markdown_content += f"```{block['language']}\n{block['content']}\n```\n\n"
    
    return markdown_content

def save_markdown(content, output_dir):
    """Save the markdown content to a file."""
    if not content:
        return None
        
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a filename from the title
    filename = re.sub(r'[^\w\s-]', '', content['title'].lower())
    filename = re.sub(r'[\s-]+', '-', filename)
    if not filename:
        filename = f"page-{hash(content['url']) % 10000}"
    
    filepath = os.path.join(output_dir, f"{filename}.md")
    
    # Write the markdown content to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(convert_to_markdown(content))
    
    return filepath

def get_existing_files(output_dir):
    """Get a list of existing files in the output directory."""
    if not os.path.exists(output_dir):
        return []
    
    files = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(output_dir, filename)
            files.append(filepath)
    
    return files

def get_urls_from_files(files):
    """Extract URLs from existing markdown files."""
    urls = set()
    
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Look for the source URL line
                match = re.search(r'Source: \[(.*?)\]', content)
                if match:
                    url = match.group(1)
                    urls.add(url)
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
    
    return urls

def read_url_list(file_path=DOCS_URL_FILE):
    """Read URLs from a text file."""
    urls = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                url = line.strip()
                if url and not url.startswith('#'):  # Skip empty lines and comments
                    urls.append(url)
        print(f"Read {len(urls)} URLs from {file_path}")
        return urls
    except Exception as e:
        print(f"Error reading URL list from {file_path}: {e}")
        return []

def crawl_docs_from_url_list(url_list, output_dir="vertex_ai_docs"):
    """Crawls documentation from a list of URLs and saves content as markdown files."""
    print(f"Starting crawl of {len(url_list)} URLs")
    
    # Get existing files and URLs
    existing_files = get_existing_files(output_dir)
    existing_urls = get_urls_from_files(existing_files)
    print(f"Found {len(existing_urls)} already crawled URLs")
    
    visited_urls = set()
    documentation_content = {}  # {url: content}
    saved_files = []

    for url in url_list:
        if url in visited_urls:
            continue
            
        if url in existing_urls:
            print(f"Skipping already crawled URL: {url}")
            continue

        print(f"Crawling: {url}")
        visited_urls.add(url)
        html = get_page_content(url)

        if html:
            # Extract content from the current page
            content = extract_content_with_code(html, url)
            if content:
                documentation_content[url] = content
                # Save content as markdown
                saved_file = save_markdown(content, output_dir)
                if saved_file:
                    saved_files.append(saved_file)
                    print(f"  -> Saved to {saved_file}")
                else:
                    print(f"  -> Failed to save content.")
            else:
                print(f"  -> No content extracted.")

            # Polite delay
            time.sleep(REQUEST_DELAY)
        else:
            print(f"  -> Failed to fetch or process.")

    print(f"\nCrawling finished. Visited {len(visited_urls)} unique URLs.")
    print(f"Successfully extracted content from {len(documentation_content)} pages.")
    print(f"Saved {len(saved_files)} markdown files to {output_dir}.")
    
    return documentation_content, saved_files

def create_semantic_search_index(mcp_registry_path, output_path="mcp_search_index.json"):
    """Create a semantic search index for MCP servers registry."""
    print(f"Creating semantic search index from {mcp_registry_path}")
    
    try:
        # Load the MCP registry JSON
        with open(mcp_registry_path, 'r') as f:
            registry_data = json.load(f)
        
        # Extract relevant information for search
        search_index = []
        
        if 'items' in registry_data:
            for item in registry_data['items']:
                server_info = {
                    'name': item.get('name', 'Unknown'),
                    'repo_url': item.get('repo_url', ''),
                    'type': item.get('type', 'unknown'),
                    'search_text': '',
                    'tools': []
                }
                
                # Extract analysis results if available
                if 'analysis_results' in item:
                    analysis = item['analysis_results']
                    
                    # Add description
                    if 'server_description' in analysis:
                        server_info['description'] = analysis['server_description']
                        server_info['search_text'] += analysis['server_description'] + " "
                    
                    # Add language stack
                    if 'language_stack' in analysis:
                        server_info['languages'] = analysis['language_stack']
                        server_info['search_text'] += " ".join(analysis['language_stack']) + " "
                    
                    # Add tools
                    if 'tools_exposed' in analysis:
                        server_info['tools'] = analysis['tools_exposed']
                        server_info['search_text'] += " ".join(analysis['tools_exposed']) + " "
                
                # Add to search index
                search_index.append(server_info)
        
        # Save the search index
        with open(output_path, 'w') as f:
            json.dump(search_index, f, indent=2)
        
        print(f"Created search index with {len(search_index)} entries at {output_path}")
        return search_index
    
    except Exception as e:
        print(f"Error creating search index: {e}")
        return None

def main():
    """Main function to run the crawler and create search index."""
    # Define output directory relative to the script's location
    docs_output_dir = "../docs/vertex_ai_docs"
    os.makedirs(docs_output_dir, exist_ok=True) # Ensure the target directory exists
    
    # Read URLs from file
    url_list = read_url_list()
    if not url_list:
        print("No URLs found to crawl. Exiting.")
        return
    
    # Crawl documentation from URL list
    print("Starting documentation crawler...")
    crawl_docs_from_url_list(url_list, output_dir=docs_output_dir)
    
    # Create semantic search index for MCP servers
    print("\nCreating semantic search index for MCP servers...")
    # Paths relative to the script's location in mcp-search/scripts/
    mcp_registry_path = "../mcp_servers_registry.json"
    search_index_path = "../docs/mcp_search_index.json"
    create_semantic_search_index(mcp_registry_path, search_index_path)
    
    print("\nAll tasks completed successfully!")

if __name__ == "__main__":
    main()