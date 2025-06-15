from fastmcp import FastMCP
from db import add_user, get_user
from models import init_db

mcp = FastMCP("Vulnerable MCP 🕷️")

# Initialisation DB au démarrage
init_db()

@mcp.tool
def register(username: str, password: str) -> str:
    add_user(username, password)
    return f"User {username} registered!"

@mcp.tool
def login(username: str, password: str) -> str:
    user = get_user(username)
    if user and user[2] == password:
        return f"Login OK for {username}"
    else:
        return "Invalid credentials"

@mcp.tool
def list_users() -> str:
    # Vulnérable : pas de restriction, tout le monde peut lister
    from sqlite3 import connect
    conn = connect("mcp_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return ", ".join(users)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000, path="/mcp")
