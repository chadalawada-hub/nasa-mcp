# Build Your First MCP Server: A Practical Guide Using NASA APIs

> **Learn Model Context Protocol (MCP) by wrapping familiar APIs**

This repository serves as a hands-on tutorial for building your first MCP (Model Context Protocol) server. We use NASA's public APIs as examples because they're well-documented, free, and interesting to work with. The techniques shown here can be applied to wrap any REST API as an MCP server.

## What You'll Learn

- How to structure an MCP server project
- Converting REST API calls into MCP tools
- Handling API authentication and error management
- Testing your MCP server with MCP Inspector, Claude Desktop, and Postman

## Why This Tutorial Exists

Most developers are already familiar with REST APIs, but MCP is relatively new. This tutorial bridges that gap by showing you how to take any API you know and make it available to AI assistants through the MCP protocol.

## Adapting This for Your Customized MCP Server
1. **Replace the API client** ( → `api/your_api.py`) `api/nasa.py`
2. **Update the MCP tools** (modify ) `nasa_mcp_server.py`
3. **Change environment variables** (update ) `.env`


## Video Walkthrough
[youtube link](https://youtu.be/6u2PdT9DvII)

## License
MIT License - Feel free to use this as a template for your own MCP servers!
**Remember**: The goal isn't to build the perfect NASA server—it's to learn the patterns that work for any API. Start here, then build something amazing with your favorite APIs!


Account Email: kostavila@gmail.com
Account ID: acd8e1ba-d318-46f9-9ef2-3d473568fa1b