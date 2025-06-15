import sqlite3

def init_db():
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()

    # Table des secrets (déjà existante)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS secrets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        secret TEXT
    )
    """)
    cursor.execute("INSERT OR IGNORE INTO secrets (id, secret) VALUES (1, 'TOP_SECRET_PASSWORD')")

    # Nouvelle table : users + cartes replace if table exists
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        amount INTEGER,
        credit_card TEXT
    )
    """)

    # Insère quelques utilisateurs
    users = [
        ("alice", 12, "4111111111111111"),
        ("bob", 8, "5500000000000004"),
        ("charlie", 5, "340000000000009"),
        ("dave", 20, "6011000990139424"),
        ("eve", 15, "30000000000004")
    ]
    cursor.executemany("INSERT OR IGNORE INTO users (username, amount, credit_card) VALUES (?, ?, ?)", users)
    

    conn.commit()
    conn.close()

# Requête safe pour débogage
def get_users():
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    data = cursor.fetchall()
    conn.close()
    return data

# ⚠️ Requête vulnérable à SQL Injection !
def search_user_raw(query: str):
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    # ⚠️ Concaténation directe => vulnérable
    cursor.execute(f"SELECT username, credit_card FROM users WHERE username LIKE '%{query}%'")
    data = cursor.fetchall()
    conn.close()
    return data

def execute_raw_query(query: str):
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        conn.commit()
        return data
    except Exception as e:
        return f"Error executing query: {e}"
    finally:
        conn.close()


def get_amount_db(username: str):
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    #query = f"SELECT amount FROM users WHERE username LIKE '{username}'" 
    query = f"SELECT username, amount, credit_card FROM users WHERE username LIKE '%{username}%'"
    query = f"SELECT username, amount FROM users WHERE username LIKE '{username}'"
    cursor.execute(query)
    #cursor.execute(f"SELECT amount FROM users WHERE username LIKE '{username}'")
    data = cursor.fetchall()
    print(f"Executing query: {query}")
    print(f"data: {data}")
    conn.close()
    return data if data else None