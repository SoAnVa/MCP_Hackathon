from smolagents import tool
from db import get_users, search_user_raw, execute_raw_query, get_amount_db

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

@tool
def execute_sql(query: str) -> str:
    """Execute a raw SQL query
    Args:
        query (str): The SQL query to execute
    Returns:
        str: The result of the query
    """
    return str(execute_raw_query(query))

@tool
def get_amount(username: str) -> str:
    """Get the amount for a user
    Args:
        username (str): The name of the user
    Returns:
        str: The amount for the user
    """
    amount = get_amount_db(username)
    return f"The amount for {username} is {amount}"