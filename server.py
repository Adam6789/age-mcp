from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
import uvicorn
import os

print("🚀 MCP server starting...")

security = TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=[
        "localhost",
        "127.0.0.1",
        "age-mcp.onrender.com",
        "*.onrender.com",
    ],
)

mcp = FastMCP(
    "age-server",
    transport_security=security,
)

@mcp.tool()
def get_age_by_name(name: str) -> int:
    return {"Hans": 52, "Peter": 28}.get(name, -1)

app = mcp.sse_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        proxy_headers=True,
        forwarded_allow_ips="*",
    )