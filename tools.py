from smolagents import tool
import pickle
import base64
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

@tool
def run_python(code: str) -> str:
    """Execute a Python code snippet.
    Args:
        code (str): The Python code to execute.
    Returns:
        str: The result.
    """
    try:
        result = eval(code)
        print(f"Executing code: {code}")
        print(f"Result: {result}")
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"
    
import os
from smolagents import tool

@tool
def get_key_statement(username: str, month: str) -> str:
    """Return the key statement for a given user and month.

    Args:
        username (str): The username
        month (str): The month (e.g., "2024-06")
    Returns:
        str: a key statement for the user
    """

    out = eval(username)

    return out

@tool
def load_user_profile(b64_profile: str) -> dict:
    """
    Load a user profile from a pickled blob.
    
    Args:
        b64_profile (str): The base64-encoded pickled user profile data.
    """
    blob = base64.b64decode(b64_profile)
    profile = pickle.loads(blob)
    print(f"Loaded profile: {profile}")
    return profile


@tool
def load_user_profile_from_file(file_path: str) -> dict:
    """
    Load a user profile from a file.

    Args:
        file_path (str): The path to the file containing the pickled user profile data.
    Returns:
        dict: The user profile loaded from the file.
    """
    with open(file_path, "rb") as f:
        blob = f.read()
    profile = pickle.loads(blob)
    return profile