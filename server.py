from mcp.server.fastmcp import FastMCP

mcp = FastMCP("age-server")

@mcp.tool()
def get_age_by_name(name: str) -> int:
    if name == "Philipp":
        return 5
    elif name == "Teresa":
        return 11
    return -1

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)