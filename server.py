import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("age-server")


@mcp.tool()
def get_age_by_name(name: str) -> int:
    if name == "Hans":
        return 52
    elif name == "Peter":
        return 28
    return -1


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port
    )