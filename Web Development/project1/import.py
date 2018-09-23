import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.sql import text
from tqdm import tqdm

engine = create_engine(os.getenv("DATABASE_URL"))
conn = engine.connect()

# conn.execute("""
# DROP TABLE IF EXISTS Authors;
# DROP TABLE IF EXISTS Books;
#
# CREATE TABLE Authors (
#     id SERIAL PRIMARY KEY,
#     name TEXT UNIQUE
# );
# CREATE TABLE Books (
#     id SERIAL PRIMARY KEY,
#     isbn TEXT UNIQUE,
#     title TEXT,
#     year INTEGER,
#     author_id INTEGER
# );
# """)

with open("books.csv") as f:
    for line in tqdm(csv.DictReader(f)):
        st = text("""SELECT id FROM Books WHERE isbn=:isbn""")
        if conn.execute(st, line).fetchone():
            continue

        st = text("""INSERT INTO Authors (name) VALUES (:author) ON CONFLICT DO NOTHING""")
        conn.execute(st, line)

        st = text("""SELECT id FROM Authors WHERE name=:author""")
        author_id = conn.execute(st, line).fetchone()[0]

        line["author_id"] = author_id
        st = text("""INSERT INTO Books (isbn, title, year, author_id)
                     VALUES (:isbn, :title, :year, :author_id)
                     ON CONFLICT DO NOTHING""")
        conn.execute(st, line)




conn.close()
