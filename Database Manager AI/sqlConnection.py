import sqlite3 as sq
from pathlib import Path
print(Path(__file__).parent)
connection = sq.connect(f"{Path(__file__).parent}/student.db")

cursor = connection.cursor()


DATA = cursor.execute('''
SELECT * FROM CLASS;
''')
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in DB:", tables)
print(DATA.fetchall())

connection.commit()
connection.close()
