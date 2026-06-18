from starlette.middleware.trustedhost import TrustedHostMiddleware
from mcp.server.fastmcp import FastMCP
import uvicorn
import os

print("🚀 MCP server starting...")
mcp = FastMCP("age-server")
app = mcp.streamable_http_app()

app.add_middleware(TrustedHostMiddleware, allowed_hosts=[
    "age-mcp.onrender.com",
    "*.onrender.com",
    "localhost",
    "127.0.0.1",
], )

@mcp.tool()
def get_age_by_name(name: str) -> int:
    return {"Hans": 52, "Peter": 28}.get(name, -1)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

