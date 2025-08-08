import sqlite3


def init_db():
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER,
                note TEXT
            )
        """)
        conn.commit()

def add_note(note: str):
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users(note) VALUES (?)",(note,))
        conn.commit()

def get_note(user_id: int):
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT note FROM users WHERE user_id=?", (user_id,))
        row = cur.fetchall()
        return [r[0] for r in row]

def del_note(note: str):
    with sqlite3.connect('book.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE note=?",(note,))
        conn.commit()