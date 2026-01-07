import sqlite3

db_file = "data/gestore.db"

def get_connection():
    return sqlite3.connect(db_file)
