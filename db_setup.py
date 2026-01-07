import sqlite3

conn = sqlite3.connect("data/orchestrator.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS jobs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    payload TEXT,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Tabella jobs creata correttamente!")