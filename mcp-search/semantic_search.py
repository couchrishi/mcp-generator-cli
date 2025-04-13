import os
import json
import glob
import argparse
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Default paths
DOCS_DIR = "vertex_ai_docs"
MCP_REGISTRY_PATH = "mcp_servers_registry.json"
MCP_SEARCH_INDEX_PATH = "mcp_search_index.json"
EMBEDDINGS_PATH = "embeddings.npz"

class SemanticSearch:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """Initialize the semantic search with a sentence transformer model."""
        print(f"Loading sentence transformer model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.docs = []
        self.mcp_servers = []
        self.doc_embeddings = None
        self.mcp_embeddings = None
    
    def load_documentation(self, docs_dir=DOCS_DIR):
        """Load documentation from markdown files."""
        print(f"Loading documentation from {docs_dir}")
        self.docs = []
        
        # Find all markdown files
        md_files = glob.glob(os.path.join(docs_dir, "*.md"))
        
        for file_path in md_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Extract title from the first line if it starts with #
                    lines = content.split('\n')
                    title = lines[0].strip('# ') if lines and lines[0].startswith('# ') else Path(file_path).stem
                    
                    # Get the text content (skip the title)
                    text = '\n'.join(lines[1:])
                    
                    self.docs.append({
                        'title': title,
                        'path': file_path,
                        'content': text
                    })
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
        
        print(f"Loaded {len(self.docs)} documentation files")
    
    def load_mcp_servers(self, registry_path=MCP_REGISTRY_PATH, search_index_path=MCP_SEARCH_INDEX_PATH):
        """Load MCP servers from registry or search index."""
        print(f"Loading MCP servers")
        
        # Try to load from search index first
        if os.path.exists(search_index_path):
            try:
                with open(search_index_path, 'r') as f:
                    self.mcp_servers = json.load(f)
                print(f"Loaded {len(self.mcp_servers)} MCP servers from search index")
                return
            except Exception as e:
                print(f"Error loading search index: {e}")
        
        # Fall back to registry if search index not available
        if os.path.exists(registry_path):
            try:
                with open(registry_path, 'r') as f:
                    registry_data = json.load(f)
                
                self.mcp_servers = []
                
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
                        self.mcp_servers.append(server_info)
                
                print(f"Loaded {len(self.mcp_servers)} MCP servers from registry")
                
                # Save as search index for future use
                with open(search_index_path, 'w') as f:
                    json.dump(self.mcp_servers, f, indent=2)
                print(f"Saved search index to {search_index_path}")
            except Exception as e:
                print(f"Error loading registry: {e}")
    
    def create_embeddings(self):
        """Create embeddings for documentation and MCP servers."""
        print("Creating embeddings...")
        
        # Create embeddings for documentation
        if self.docs:
            doc_texts = [f"{doc['title']}\n{doc['content']}" for doc in self.docs]
            self.doc_embeddings = self.model.encode(doc_texts)
            print(f"Created embeddings for {len(self.docs)} documentation files")
        
        # Create embeddings for MCP servers
        if self.mcp_servers:
            mcp_texts = []
            for server in self.mcp_servers:
                text = f"{server['name']}"
                if 'description' in server:
                    text += f"\n{server['description']}"
                if 'search_text' in server and server['search_text']:
                    text += f"\n{server['search_text']}"
                mcp_texts.append(text)
            
            self.mcp_embeddings = self.model.encode(mcp_texts)
            print(f"Created embeddings for {len(self.mcp_servers)} MCP servers")
    
    def save_embeddings(self, path=EMBEDDINGS_PATH):
        """Save embeddings to file."""
        if self.doc_embeddings is not None and self.mcp_embeddings is not None:
            np.savez(
                path,
                doc_embeddings=self.doc_embeddings,
                mcp_embeddings=self.mcp_embeddings
            )
            print(f"Saved embeddings to {path}")
    
    def load_embeddings(self, path=EMBEDDINGS_PATH):
        """Load embeddings from file."""
        if os.path.exists(path):
            try:
                data = np.load(path)
                self.doc_embeddings = data['doc_embeddings']
                self.mcp_embeddings = data['mcp_embeddings']
                print(f"Loaded embeddings from {path}")
                return True
            except Exception as e:
                print(f"Error loading embeddings: {e}")
        return False
    
    def search(self, query, top_k=5):
        """Search for relevant documentation and MCP servers."""
        print(f"Searching for: {query}")
        
        # Encode the query
        query_embedding = self.model.encode([query])[0]
        
        results = {
            'docs': [],
            'mcp_servers': []
        }
        
        # Search documentation
        if self.doc_embeddings is not None and len(self.docs) > 0:
            # Calculate similarity scores
            doc_scores = cosine_similarity([query_embedding], self.doc_embeddings)[0]
            
            # Get top k results
            top_doc_indices = doc_scores.argsort()[-top_k:][::-1]
            
            for idx in top_doc_indices:
                results['docs'].append({
                    'title': self.docs[idx]['title'],
                    'path': self.docs[idx]['path'],
                    'score': float(doc_scores[idx]),
                    'excerpt': self.docs[idx]['content'][:200] + "..."  # Short excerpt
                })
        
        # Search MCP servers
        if self.mcp_embeddings is not None and len(self.mcp_servers) > 0:
            # Calculate similarity scores
            mcp_scores = cosine_similarity([query_embedding], self.mcp_embeddings)[0]
            
            # Get top k results
            top_mcp_indices = mcp_scores.argsort()[-top_k:][::-1]
            
            for idx in top_mcp_indices:
                server = self.mcp_servers[idx]
                result = {
                    'name': server['name'],
                    'repo_url': server['repo_url'],
                    'score': float(mcp_scores[idx])
                }
                
                # Add description if available
                if 'description' in server:
                    result['description'] = server['description']
                
                # Add tools if available
                if 'tools' in server and server['tools']:
                    result['tools'] = server['tools']
                
                results['mcp_servers'].append(result)
        
        return results
    
    def print_search_results(self, results):
        """Print search results in a readable format."""
        print("\n=== Documentation Results ===")
        if results['docs']:
            for i, doc in enumerate(results['docs']):
                print(f"{i+1}. {doc['title']} (Score: {doc['score']:.4f})")
                print(f"   Path: {doc['path']}")
                print(f"   Excerpt: {doc['excerpt']}")
                print()
        else:
            print("No documentation results found.")
        
        print("\n=== MCP Server Results ===")
        if results['mcp_servers']:
            for i, server in enumerate(results['mcp_servers']):
                print(f"{i+1}. {server['name']} (Score: {server['score']:.4f})")
                print(f"   Repo: {server['repo_url']}")
                
                if 'description' in server:
                    print(f"   Description: {server['description']}")
                
                if 'tools' in server and server['tools']:
                    print(f"   Tools: {', '.join(server['tools'])}")
                
                print()
        else:
            print("No MCP server results found.")

def main():
    """Main function to run the semantic search."""
    parser = argparse.ArgumentParser(description="Semantic search for MCP servers and documentation")
    parser.add_argument("--query", "-q", type=str, help="Search query")
    parser.add_argument("--docs-dir", type=str, default=DOCS_DIR, help="Documentation directory")
    parser.add_argument("--registry", type=str, default=MCP_REGISTRY_PATH, help="MCP registry path")
    parser.add_argument("--index", type=str, default=MCP_SEARCH_INDEX_PATH, help="MCP search index path")
    parser.add_argument("--embeddings", type=str, default=EMBEDDINGS_PATH, help="Embeddings file path")
    parser.add_argument("--top-k", type=int, default=5, help="Number of top results to return")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild embeddings")
    args = parser.parse_args()
    
    # Initialize semantic search
    search = SemanticSearch()
    
    # Load data
    search.load_documentation(args.docs_dir)
    search.load_mcp_servers(args.registry, args.index)
    
    # Load or create embeddings
    if not args.rebuild and search.load_embeddings(args.embeddings):
        print("Using existing embeddings")
    else:
        search.create_embeddings()
        search.save_embeddings(args.embeddings)
    
    # If query is provided, perform search
    if args.query:
        results = search.search(args.query, args.top_k)
        search.print_search_results(results)
    else:
        # Interactive mode
        print("\nEnter search queries (type 'exit' to quit):")
        while True:
            query = input("\nSearch query: ")
            if query.lower() in ['exit', 'quit', 'q']:
                break
            
            if query.strip():
                results = search.search(query, args.top_k)
                search.print_search_results(results)

if __name__ == "__main__":
    main()