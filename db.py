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

    # Nouvelle table : users + cartes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        credit_card TEXT
    )
    """)

    # Insère quelques utilisateurs
    users = [
        ("alice", "4111 1111 1111 1111"),
        ("bob", "5500 0000 0000 0004"),
        ("charlie", "3400 0000 0000 009")
    ]
    cursor.executemany("INSERT OR IGNORE INTO users (id, username, credit_card) VALUES (?, ?, ?)",
                       [(i+1, u[0], u[1]) for i, u in enumerate(users)])

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
