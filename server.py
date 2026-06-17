from mcp.server.fastmcp import FastMCP

mcp = FastMCP("age-server")


@mcp.tool()
def get_age_by_name(name: str) -> int:
    return {"Hans": 52, "Peter": 28}.get(name, -1)


if __name__ == "__main__":
    mcp.run(transport="sse")