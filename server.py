print("🚀 MCP server starting...")

from mcp.server.fastmcp import FastMCP
import uvicorn
import os

mcp = FastMCP("age-server")
app = mcp.sse_app()

@mcp.tool()
def get_age_by_name(name: str) -> int:
    return {"Hans": 52, "Peter": 28}.get(name, -1)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port)

