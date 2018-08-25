import sqlite3, json

conn = sqlite3.connect('studentdb.sqlite')
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Funct;

CREATE TABLE Student (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                      name TEXT UNIQUE);
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                     name TEXT UNIQUE);
CREATE TABLE Funct (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                   name TEXT UNIQUE);
CREATE TABLE Member (student_id INTEGER,
                     course_id INTEGER,
                     funct_id INTEGER,
                     PRIMARY KEY (student_id, course_id));

INSERT INTO Funct (name) VALUES ("student");
INSERT INTO Funct (name) VALUES ("teacher");
""")
with open("sample.json") as f:
    data = json.load(f)
    for val in data:
        student_name = val[0]
        course_name = val[1]
        role = val[2]

        cur.execute("INSERT OR IGNORE INTO Student (name) VALUES (?)",
                    (student_name, ))
        student_id = cur.execute("SELECT id FROM Student WHERE name=?",
                                 (student_name, )).fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Course (name) VALUES (?)",
                    (course_name, ))
        course_id = cur.execute("SELECT id FROM Course WHERE name=?",
                                (course_name, )).fetchone()[0]

        cur.execute("""INSERT OR IGNORE INTO Member (student_id, course_id, funct_id)
                       VALUES (?, ?, ?)""", (student_id, course_id, role + 1))
    conn.commit()

cur.execute("""SELECT Student.name, Course.name, Funct.name
               FROM Member JOIN Student JOIN Course JOIN Funct
               ON Student.id = Member.student_id AND
                  Course.id = Member.course_id AND
                  Member.funct_id = Funct.id
            """)

for rec in cur.fetchall():
    print(rec)
