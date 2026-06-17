from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP("age-server")


@mcp.tool()
def get_age_by_name(name: str) -> int:
    if name == "Philipp":
        return 5
    elif name == "Teresa":
        return 11
    return -1


@app.get("/health")
def health():
    return {"status": "ok"}