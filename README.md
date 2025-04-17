# 🎓 Semantic Scholar MCP Server

[![smithery badge](https://smithery.ai/badge/@JackKuo666/semanticscholar-mcp-server)](https://smithery.ai/server/@JackKuo666/semanticscholar-mcp-server)

This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

## ✨ Features

- 🔍 Search for papers on Semantic Scholar
- 📄 Retrieve detailed information about specific papers
- 👤 Get author details
- 🔗 Fetch citations and references for a paper

## 🚀 Installation
### Installing via Smithery

To install semanticscholar Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@JackKuo666/semanticscholar-mcp-server):

#### claude

```sh
npx -y @smithery/cli@latest install @JackKuo666/semanticscholar-mcp-server --client claude --config "{}"
```

#### Cursor

Paste the following into Settings → Cursor Settings → MCP → Add new server: 
- Mac/Linux  
```s
npx -y @smithery/cli@latest run @JackKuo666/semanticscholar-mcp-server --client cursor --config "{}" 
```
#### Windsurf
```sh
npx -y @smithery/cli@latest install @JackKuo666/semanticscholar-mcp-server --client windsurf --config "{}"
```
#### CLine
```sh
npx -y @smithery/cli@latest install @JackKuo666/semanticscholar-mcp-server --client cline --config "{}"
```

### Installing Manually
[UV](https://github.com/astral-sh/uv) is a modern Python package manager and environment manager. Here's how to use it with this project:

```bash
uv tool install git+https://github.com/JackKuo666/semanticscholar-MCP-Server.git
```
Test:
```bash
semanticscholar-mcp serve
# output:
# Starting Semantic Scholar MCP server
```
ctrl + c to stop the server

### Installing for Developers

1. Clone this repository:
```
git clone https://github.com/JackKuo666/semanticscholar-MCP-Server.git
cd semanticscholar-mcp-server
```

2. Install the dependencies:
```
uv sync
```

3. Run the server:
```
uv run semantic_scholar_server.py
```

4. Run the CLI:
```
uv run semantic_scholar_cli.py
```

## 🖥️ Usage

If you install the server via `uv` to local, you can use the following configuration for different clients:

### Claude Desktop & Cursor & Cline

Add this configuration to your `claude_desktop_config.json`, `cursor_config.json` or other config files:

```json
{
  "mcpServers": {
    "semanticscholar": {
      "command": "semanticscholar-mcp",
      "args": ["serve"],
      "env": {},
      "disabled": false,
      "autoApprove": []
      }
  }
}
```

### Manually Start for Development

1. Start the Semantic Scholar MCP server:
```
semanticscholar-mcp serve
```

2. The server will start and listen for MCP requests.

3. Use an MCP client to interact with the server and access the following tools:

   - 🔍 `search_semantic_scholar`: Search for papers using a query string
   - 📄 `get_semantic_scholar_paper_details`: Get details of a specific paper
   - 👤 `get_semantic_scholar_author_details`: Get details of a specific author
   - 🔗 `get_semantic_scholar_citations_and_references`: Get citations and references for a paper


## 📁 File Structure

- 📜 `semantic_scholar_search.py`: Contains functions for interacting with the Semantic Scholar API
- 🖥️ `semantic_scholar_server.py`: Implements the MCP server and defines the available tools
- 📄 `semantic_scholar_cli.py`: Implements the MCP server and defines the available tools

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
