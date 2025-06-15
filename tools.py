from smolagents import tool
from db import get_users, search_user_raw

@tool
def hello_world(name: str) -> str:
    """Say hello to the user

    Args:
        name (str): The name of the user
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


@tool
def list_users() -> str:
    """List all users in the database
    Args:
        None
    Returns:
        str: All users in the database
    """
    return str(get_users())

# ⚠️ Tool vulnérable : injection possible
@tool
def search_user(query: str) -> str:
    """Search for a user by name
    Args:
        query (str): The name of the user to search for
    Returns:
        str: The user information
    """
    return str(search_user_raw(query))
