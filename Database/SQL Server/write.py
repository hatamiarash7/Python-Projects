import pymssql

server = "HATAMIARASH7"
user = "sa"
password = "3920512197"
database = "Movie"

conn = pymssql.connect(server, user, password, database)
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS test""")
cur.execute("""CREATE TABLE test(
                    id INT NOT NULL PRIMARY KEY,
                    fname NVARCHAR(10),
                    lname NVARCHAR(20)
                    )""")
cur.executemany(
    "INSERT INTO test VALUES (%d, %s, %s)",
    [(1, 'Arash', 'Hatami'),
     (2, 'Sina', 'Rasooli'),
     (3, 'Javad', 'Ezati')])

conn.commit()
conn.close()
