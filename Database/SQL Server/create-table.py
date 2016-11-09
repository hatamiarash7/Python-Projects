import pymssql

server = "HATAMIARASH7"
user = "sa"
password = "3920512197"
database = "Movie"

conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()
cursor.execute("""create table test(a nvarchar(4)not null);""")

conn.commit()
conn.close()
