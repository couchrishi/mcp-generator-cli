# MCP Server Generator CLI

A command-line tool for generating customized MCP servers based on natural language descriptions.

## Overview

The MCP Server Generator CLI addresses the challenge of tool/function limits in development environments like Cursor or Roo Code by creating hybrid MCP servers with only the necessary tools across multiple service providers.

## Installation

```bash
npm install -g mcp-generator-cli
```

Or use it directly with npx:

```bash
npx generate-mcp-server [options]
```

## Usage

```bash
npx generate-mcp-server [options]

Options:
  -p, --project <path>    Path to existing project
  -d, --description <path>    Path to project description file
  -o, --output <path>     Output directory for generated files
  -h, --help              Display help information
  -v, --verbose           Enable verbose logging
```

### Interactive Mode

If you run the command without options, it will start in interactive mode and prompt you for:

1. Project type selection (new or existing)
2. Project path
3. Project description (direct input or file path)
4. Output directory

### Examples

Generate an MCP server for an existing project:

```bash
npx generate-mcp-server --project ./my-project --description ./description.txt --output ./mcp-server
```

Generate an MCP server with direct description input:

```bash
npx generate-mcp-server --project ./my-project --output ./mcp-server
```

## Features

- Generate customized MCP servers based on natural language descriptions
- Support for existing and new projects
- Interactive command-line interface
- Integration with multiple service providers (GitHub, Slack, Jira, etc.)
- Optimized tool selection based on project requirements

## Development

### Prerequisites

- Node.js 14.x or higher
- npm 6.x or higher

### Setup

1. Clone the repository
2. Install dependencies:

```bash
npm install
```

3. Run the CLI:

```bash
npm start
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT