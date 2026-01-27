import sqlite3
from datetime import datetime

DB_NAME = "di3.db"

def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # 1) Tabel maken
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    # 2) Sample data toevoegen (als leeg)
    cur.execute("SELECT COUNT(*) FROM notes")
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO notes (title, created_at) VALUES (?, ?)",
                    ("Di3 SQL experiment werkt", datetime.now().isoformat()))
        cur.execute("INSERT INTO notes (title, created_at) VALUES (?, ?)",
                    ("SQLite draait in Docker", datetime.now().isoformat()))
        conn.commit()

    # 3) SELECT bewijs
    cur.execute("SELECT id, title, created_at FROM notes ORDER BY id")
    rows = cur.fetchall()

    print("=== Di3 SQL RESULT (SELECT) ===")
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]}")

    conn.close()

if __name__ == "__main__":
    main()
