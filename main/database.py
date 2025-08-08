import sqlite3


def init_db():
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                mentions TEXT
            )
        """)
        conn.commit()

def add_mentions(mentions: str):
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users(mentions) VALUES (?)",(mentions,))
        conn.commit()

def get_mentions(user_id: int):
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT mentions FROM users WHERE user_id=?", (user_id,))
        row = cur.fetchall()
        return [row[0] for row in row]

def del_mentions(mentions: str):
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM user WHERE mentions=?",(mentions,))
        conn.commit()