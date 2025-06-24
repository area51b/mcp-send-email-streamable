from mcp.server.fastmcp import FastMCP
from src.config.settings import (
    MCP_SERVER_NAME,
    MCP_SERVER_PORT,
    MCP_STATELESS_HTTP
)
from src.tools.mcp_tools import register_tools

def main():
    # Initialize FastMCP server
    mcp = FastMCP(
        MCP_SERVER_NAME,
        host="0.0.0.0",
        port=MCP_SERVER_PORT,
        stateless_http=MCP_STATELESS_HTTP
    )
    
    # Register all tools
    register_tools(mcp)
    
    # Run the server
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
