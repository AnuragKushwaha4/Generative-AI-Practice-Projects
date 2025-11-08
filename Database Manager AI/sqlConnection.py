import sqlite3 as sq
from pathlib import Path
print(Path(__file__).parent)
connection = sq.connect(f"{Path(__file__).parent}/student.db")

cursor = connection.cursor()


DATA = cursor.execute('''
SELECT * FROM CLASS;
''')

print(DATA.fetchall())

connection.commit()
connection.close()
