from mcp.server.fastmcp import FastMCP

def register_tools(mcp: FastMCP):
    """Register cluster-related tools with the MCP server."""
    
    @mcp.tool()
    async def hello_world() -> str:
        """Return a simple Hello World message."""
        return "Hello, world!"

    @mcp.prompt()
    async def sample_prompt() -> str:
        """A sample MCP prompt that returns a static message."""
        return "This is a sample MCP prompt."
