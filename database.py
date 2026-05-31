import sqlite3

def get_connection():
    conn = sqlite3.connect("app.db")
    return conn

def get_user(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + str(id))
    return cursor.fetchone()