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
    mcp.run(transport="sse")