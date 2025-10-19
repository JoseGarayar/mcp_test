# MCP Employee API Server

A Model Context Protocol (MCP) server that provides tools for managing employee data through a REST API. This server exposes employee management operations as MCP tools that can be used by AI assistants and other MCP clients.

## Features

- **Employee Management**: Full CRUD operations for employee data
- **REST API Integration**: Connects to a local employee API server
- **MCP Protocol**: Exposes functionality through the Model Context Protocol
- **Async Operations**: Built with async/await for optimal performance
- **Error Handling**: Robust error handling for API requests

## Available Tools

The server provides the following MCP tools:

- `get_employees()` - Retrieve all employees
- `get_employee(id)` - Get a specific employee by ID
- `add_employee(name, age)` - Create a new employee
- `update_employee(id, name, age)` - Update an existing employee
- `delete_employee(id)` - Delete an employee by ID

## Prerequisites

- Python 3.13 or higher
- A running employee API server at `http://localhost:8000`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp_test
   ```

2. Clone the api employee repository:
    ```bash
   git clone <repository-url>
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Usage

### Running the MCP Server

Start the MCP server using stdio transport:

```bash
uv run python main.py
```

The server will run and listen for MCP protocol messages via stdin/stdout.

### API Configuration

The server is configured to connect to a local API server at `http://localhost:8000`. You can modify the `URL_BASE` constant in `main.py` to point to a different API endpoint.

### Example API Endpoints

The server expects the following API endpoints to be available:

- `GET /employees` - List all employees
- `GET /employees/{id}` - Get employee by ID
- `POST /employees` - Create new employee
- `PUT /employees/{id}` - Update employee
- `DELETE /employees/{id}` - Delete employee

## Development

### Project Structure

```
mcp_test/
├── main.py          # Main MCP server implementation
├── pyproject.toml   # Project configuration and dependencies
├── README.md        # This file
└── uv.lock         # Lock file for dependencies
```

### Dependencies

- `httpx` - Async HTTP client for API requests
- `mcp[cli]` - Model Context Protocol implementation

### Development Dependencies

- `ruff` - Python linter and formatter

## Error Handling

The server includes comprehensive error handling:

- Network timeouts (30 seconds)
- HTTP error status codes
- Invalid HTTP methods
- Connection failures

All errors are gracefully handled and return `None` for failed operations.

## License

This project is part of a test implementation for MCP server development.
