import sqlite3, sys

def get_mails(file):
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Counts")
    cur.execute("""CREATE TABLE Counts(
                       email VARCHAR(20),
                       count INTEGER
                   )""")

    with open(file) as f:
        for line in f:
            if not line.startswith("From:"): continue
            data = line.split()[1]

            cur.execute("SELECT email FROM Counts WHERE email=?", (data, ))
            if cur.fetchone() == None:
                cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (data, ))
            else:
                cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (data, ))
        conn.commit()


    for n in cur.execute("SELECT * FROM Counts ORDER BY count DESC LIMIT 5"):
        print("Email: {} appears: {} times".format(n[0], n[1]))
    cur.close()

if __name__ == "__main__":
    get_mails(sys.argv[1])
