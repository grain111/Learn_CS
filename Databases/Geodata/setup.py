import sqlite3

conn = sqlite3.connect("raw_data.sqlite")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS Places;
CREATE TABLE Places (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    data TEXT
    );
""")
