from smolagents import tool
import pickle
from db import get_users, get_amount_db

@tool
def list_users() -> str:
    """List all users in the database
    Args:
        None
    Returns:
        str: All users in the database
    """
    return str(get_users())

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

@tool
def load_user_profile_from_file(file_path: str) -> dict:
    """
    Load a user profile from a file.

    Args:
        file_path (str): The path to the file containing the pickled user profile data.
    Returns:
        dict: The user profile loaded from the file.
    """
    with open(f'./data/{file_path}', "rb") as f:
        blob = f.read()
    profile = pickle.loads(blob)
    return profile