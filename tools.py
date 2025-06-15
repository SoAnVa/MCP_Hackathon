from smolagents import tool
from db import get_all_secrets

@tool
def hello_world(name: str) -> str:
    """
    Simple tool that greets the user by name.

    Args:
        name (str): The name of the user to greet.
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

# ⚠️ Vulnérabilité : tool exposant directement la DB sans filtrer
@tool
def leak_secrets() -> str:
    """
    Tool that leaks all secrets from the database.
    This is a security vulnerability as it exposes sensitive information.

    Args:
        None
    Returns:
        str: A string representation of all secrets in the database.
    """
    # Directly returning all secrets without any access control
    return str(get_all_secrets())