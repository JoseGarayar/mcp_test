from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("api-employees")

# Constants
URL_BASE = "http://localhost:8000"
USER_AGENT = "api-employees/1.0"


async def make_request(url: str, method: str = "GET", json_data: dict = None) -> dict[str, Any] | None:
    """Make a request to the API with proper error handling for all HTTP methods."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    
    # Add Content-Type header for requests with JSON data
    if json_data is not None:
        headers["Content-Type"] = "application/json"
    
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers, timeout=30.0)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=json_data, timeout=30.0)
            elif method.upper() == "PUT":
                response = await client.put(url, headers=headers, json=json_data, timeout=30.0)
            elif method.upper() == "DELETE":
                response = await client.delete(url, headers=headers, timeout=30.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_employees() -> dict:
    url = f"{URL_BASE}/employees"
    response = await make_request(url)
    return response

@mcp.tool()
async def get_employee(id: int) -> dict:
    url = f"{URL_BASE}/employees/{id}"
    response = await make_request(url)
    return response

@mcp.tool()
async def add_employee(name: str, age: int) -> dict:
    url = f"{URL_BASE}/employees"
    response = await make_request(url, "POST", {
        "name": name,
        "age": age
    })
    return response

@mcp.tool()
async def update_employee(id: int, name: str, age: int) -> dict:
    url = f"{URL_BASE}/employees/{id}"
    response = await make_request(url, "PUT", {
        "name": name,
        "age": age
    })
    return response

@mcp.tool()
async def delete_employee(id: int) -> dict:
    url = f"{URL_BASE}/employees/{id}"
    response = await make_request(url, "DELETE")
    return response


def main():
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
