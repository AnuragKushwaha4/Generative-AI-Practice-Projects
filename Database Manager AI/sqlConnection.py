import sqlite3 as sq

connection = sq.connect("../../DBMS/schoolDB.db")

cursor = connection.cursor()

cursor.execute("select * from teacher;")

connection.commit()
connection.close()
