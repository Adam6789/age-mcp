from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP("age-server")


@mcp.tool()
def get_age_by_name(name: str) -> int:
    if name == "Hans":
        return 52
    elif name == "Peter":
        return 28
    return -1


@app.get("/health")
def health():
    return {"status": "ok"}

app.mount("/mcp", mcp.sse_app())