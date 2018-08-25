import sqlite3
import xml.etree.ElementTree as ET

def lookup(elements, key):
    for i, e in enumerate(elements):
        if e.tag == 'key' and e.text == key:
            return elements[i+1].text


conn = sqlite3.connect('tracksdb.sqlite')
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                     name TEXT UNIQUE);

CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE);

CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE,
                    artist_id INTEGER,
                    album_id INTEGER,
                    duration INTEGER,
                    rating INTEGER)
""")

tree = ET.parse("Library.xml")
songs = tree.findall('dict/dict/dict')

for song in songs:
    track_name = lookup(song, 'Name')
    artist_name = lookup(song, 'Artist')
    album_name = lookup(song, 'Album')
    duartion = lookup(song, 'Total Time')
    rating = lookup(song, 'Rating') if lookup(song, 'Rating') != None else 0

    if artist_name == None or album_name == None or track_name == None:
        continue

    # Getting artist ID
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist_name, ))
    artist_id = cur.execute("SELECT id FROM Artist WHERE name=?",
                           (artist_name, )).fetchone()[0]

    # Getting album ID
    cur.execute("INSERT OR IGNORE INTO Album (name) VALUES (?)", (album_name, ))
    album_id = cur.execute("SELECT id FROM Album WHERE name=?",
                           (album_name, )).fetchone()[0]

    #Inserting songs

    cur.execute("""INSERT OR REPLACE INTO Track
                   (name, artist_id, album_id, duration, rating)
                   VALUES (?,?,?,?,?)""",
                (track_name, artist_id, album_id, duartion, rating))

conn.commit()

#Fetching data from database
cat = cur.execute("""SELECT Track.name, Artist.name, Album.name, Track.duration, Track.rating
                     FROM Artist JOIN Track JOIN Album
                     ON Artist.id = Track.artist_id AND Album.id = Track.album_id
                     LIMIT 10""")
for row in cat:
    print(row)
