import sqlite3

# ⚠️ Vulnérabilité : Pas de contrôle d'accès, requêtes SQL ouvertes.
def init_db():
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS secrets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        secret TEXT
    )
    """)
    cursor.execute("INSERT INTO secrets (secret) VALUES ('TOP_SECRET_PASSWORD')")
    conn.commit()
    conn.close()

def get_all_secrets():
    conn = sqlite3.connect("mcp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM secrets")
    data = cursor.fetchall()
    conn.close()
    return data
