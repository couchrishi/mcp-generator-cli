# MCP Server Generator CLI - Architecture Design

## 1. System Architecture Overview

The MCP Server Generator CLI tool follows a modular, layered architecture that separates concerns while enabling efficient data flow between components. The system is designed to be extensible, maintainable, and focused on generating customized MCP servers based on natural language descriptions.

### System Architecture Diagram (Text Description)

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MCP Server Generator CLI                      │
├─────────────┬─────────────┬─────────────┬─────────────┬─────────────┤
│             │             │             │             │             │
│  CLI        │  Project    │  LLM        │  MCP        │  Code       │
│  Interface  │  Analyzer   │  Interaction│  Registry   │  Generator  │
│             │             │  Service    │             │             │
│             │             │             │             │             │
└─────┬───────┴──────┬──────┴──────┬──────┴──────┬──────┴──────┬──────┘
      │              │              │              │              │
      │              │              │              │              │
┌─────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
│            │ │            │ │            │ │            │ │            │
│ User Input │ │ Project    │ │ LLM API    │ │ Registry   │ │ Template   │
│ Handler    │ │ Parser     │ │ Client     │ │ Manager    │ │ Engine     │
│            │ │            │ │            │ │            │ │            │
└────────────┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘
```

The architecture consists of five main components that interact with each other to fulfill the system's requirements:

1. **CLI Interface**: The entry point for user interaction
2. **Project Analyzer**: Analyzes existing projects or creates new ones
3. **LLM Interaction Service**: Communicates with the Gemini API
4. **MCP Registry**: Manages the database of available MCP servers
5. **Code Generator**: Generates the customized MCP server code

## 2. Component Descriptions and Responsibilities

### 2.1 CLI Interface

**Responsibilities:**
- Provide an interactive command-line interface for users
- Handle command-line arguments and options
- Validate user input
- Display progress indicators and results
- Manage the overall flow of the application
- Handle error messages and user feedback

### 2.2 Project Analyzer

**Responsibilities:**
- Analyze existing projects to understand requirements
- Parse package.json and other configuration files
- Extract relevant information from project structure
- Create new project structures when needed
- Provide project context for LLM processing
- Detect existing MCP server configurations

### 2.3 LLM Interaction Service

**Responsibilities:**
- Prepare context for the Gemini API
- Format project information for LLM consumption
- Send requests to the Gemini API
- Process and parse LLM responses
- Handle error cases and implement retry logic
- Extract structured data from LLM outputs

### 2.4 MCP Registry

**Responsibilities:**
- Maintain a database of available MCP servers
- Store metadata for each server including available tools
- Track version compatibility information
- Provide filtering and selection mechanisms
- Update registry data when new servers become available
- Validate server compatibility with project requirements

### 2.5 Code Generator

**Responsibilities:**
- Generate code based on templates and LLM output
- Create proper file structures for MCP servers
- Format code according to best practices
- Generate documentation for the created server
- Handle integration with existing codebases
- Implement provider-specific optimizations

## 3. Component Interactions and Data Flow

### 3.1 Overall Data Flow

1. User provides input through the CLI Interface
2. CLI Interface validates input and initiates the workflow
3. Project Analyzer processes the project (existing or new)
4. Project information is combined with user description
5. LLM Interaction Service prepares context and sends to Gemini API
6. LLM response is processed and structured
7. MCP Registry is queried to identify relevant servers and tools
8. Code Generator creates the customized MCP server
9. Generated code is presented to the user for confirmation
10. CLI Interface handles server execution or integration

### 3.2 Key Interaction Paths

#### Path 1: New Project Creation
```
CLI Interface → Project Analyzer → LLM Interaction Service → MCP Registry → Code Generator → CLI Interface
```

#### Path 2: Existing Project Analysis
```
CLI Interface → Project Analyzer → LLM Interaction Service → MCP Registry → Code Generator → CLI Interface
```

#### Path 3: Server Execution
```
CLI Interface → Code Generator → CLI Interface
```

### 3.3 Detailed Data Flow

1. **User Input to Project Analysis**
   - CLI Interface collects user input (project type, description)
   - Project Analyzer receives project path or creates new project structure
   - Project Analyzer extracts relevant information (dependencies, structure)
   - Data is formatted for LLM consumption

2. **Project Analysis to LLM Processing**
   - Project information and user description are sent to LLM Interaction Service
   - LLM Interaction Service formats the context for Gemini API
   - Gemini API processes the information and returns a response
   - LLM Interaction Service parses the response into structured data

3. **LLM Output to MCP Registry**
   - Structured data from LLM is used to query the MCP Registry
   - MCP Registry identifies relevant servers and tools
   - Selected servers and tools are returned with metadata

4. **MCP Registry to Code Generation**
   - Selected servers, tools, and LLM output are sent to Code Generator
   - Code Generator creates the customized MCP server
   - Generated code is formatted and documented
   - Files are prepared for output

5. **Code Generation to User Confirmation**
   - Generated code is presented to the user for confirmation
   - User can review and approve or request changes
   - Approved code is saved to the specified location
   - Optional server execution is initiated

## 4. File Structure

```
mcp-generator-cli/
├── bin/                      # Executable files
│   └── generate-mcp-server   # Main CLI entry point
├── src/                      # Source code
│   ├── cli/                  # CLI Interface component
│   │   ├── index.js          # Main CLI module
│   │   ├── commands/         # CLI commands
│   │   ├── prompts/          # Interactive prompts
│   │   └── utils/            # CLI utilities
│   ├── analyzer/             # Project Analyzer component
│   │   ├── index.js          # Main analyzer module
│   │   ├── parsers/          # File and project parsers
│   │   └── extractors/       # Information extractors
│   ├── llm/                  # LLM Interaction Service component
│   │   ├── index.js          # Main LLM module
│   │   ├── context/          # Context preparation
│   │   ├── parsers/          # Response parsers
│   │   └── clients/          # API clients
│   ├── registry/             # MCP Registry component
│   │   ├── index.js          # Main registry module
│   │   ├── data/             # Registry data
│   │   └── selectors/        # Server and tool selectors
│   ├── generator/            # Code Generator component
│   │   ├── index.js          # Main generator module
│   │   ├── templates/        # Code templates
│   │   ├── formatters/       # Code formatters
│   │   └── writers/          # File writers
│   └── utils/                # Shared utilities
│       ├── logger.js         # Logging utility
│       ├── config.js         # Configuration manager
│       └── errors.js         # Error handling
├── templates/                # Template files for generated code
│   ├── server/               # Server templates
│   ├── tools/                # Tool templates
│   └── providers/            # Provider templates
├── data/                     # Data files
│   └── registry/             # MCP Registry data
│       ├── servers.json      # Server definitions
│       └── tools.json        # Tool definitions
├── tests/                    # Test files
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── fixtures/             # Test fixtures
├── docs/                     # Documentation
├── package.json              # Package configuration
└── README.md                 # Project readme
```

## 5. Key Interfaces between Components

### 5.1 CLI Interface ↔ Project Analyzer

**Data Exchange:**
- CLI Interface provides project path or new project flag
- CLI Interface provides project description
- Project Analyzer returns project structure information
- Project Analyzer returns dependency information
- Project Analyzer returns existing configuration data

### 5.2 Project Analyzer ↔ LLM Interaction Service

**Data Exchange:**
- Project Analyzer provides project structure information
- Project Analyzer provides dependency information
- Project Analyzer provides existing configuration data
- LLM Interaction Service returns processed project requirements

### 5.3 LLM Interaction Service ↔ MCP Registry

**Data Exchange:**
- LLM Interaction Service provides identified tool requirements
- LLM Interaction Service provides identified provider requirements
- MCP Registry returns matching server information
- MCP Registry returns tool metadata
- MCP Registry returns compatibility information

### 5.4 MCP Registry ↔ Code Generator

**Data Exchange:**
- MCP Registry provides selected server information
- MCP Registry provides selected tool information
- MCP Registry provides API specifications
- Code Generator returns validation results

### 5.5 Code Generator ↔ CLI Interface

**Data Exchange:**
- Code Generator provides generated file information
- Code Generator provides validation results
- CLI Interface provides user confirmation
- CLI Interface provides output path

### 5.6 LLM Interaction Service ↔ Code Generator

**Data Exchange:**
- LLM Interaction Service provides structured code requirements
- LLM Interaction Service provides tool selection information
- Code Generator returns template requirements
- Code Generator returns generation results

## 6. Cross-Cutting Concerns

### 6.1 Error Handling

- Each component implements its own error handling
- Errors are propagated up the component chain
- CLI Interface presents user-friendly error messages
- Detailed error logging for debugging

### 6.2 Logging

- Centralized logging system
- Different log levels (error, warn, info, debug)
- Verbose mode for detailed logging
- Log file generation for troubleshooting

### 6.3 Configuration Management

- Central configuration system
- Environment-specific configurations
- User preferences storage
- Default settings with override capabilities

### 6.4 Security

- Secure handling of API keys and tokens
- Environment variable integration
- No hardcoded credentials
- Secure storage recommendations