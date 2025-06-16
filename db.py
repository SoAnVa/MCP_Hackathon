import sqlite3

def init_db():
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS secrets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        secret TEXT
    )
    """)
    cursor.execute("INSERT OR IGNORE INTO secrets (id, secret) VALUES (1, 'TOP_SECRET_PASSWORD')")

    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        amount INTEGER,
        credit_card TEXT
    )
    """)

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

def get_users():
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    data = cursor.fetchall()
    conn.close()
    return data


def get_amount_db(username: str):
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    query = f"SELECT username, amount FROM users WHERE username LIKE '{username}'"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data if data else None