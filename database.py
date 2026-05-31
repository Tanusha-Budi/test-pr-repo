import sqlite3
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = sqlite3.connect("app.db")
    try:
        yield conn
    finally:
        conn.close()

def get_user(id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return cursor.fetchone()