import sqlite3 as sq
from pathlib import Path

dbfile = Path(__file__).parent / "student.db"
conn = sq.connect(dbfile)
cursor = conn.cursor()

# Optional: drop table to start fresh
cursor.execute("DROP TABLE IF EXISTS CLASS;")

# Create table
cursor.execute('''
CREATE TABLE CLASS (
    ID INT PRIMARY KEY,
    NAME VARCHAR(30),
    STANDARDS VARCHAR(10),
    HOBBY VARCHAR(40),
    MARKS INT
)
''')

# Insert data
cursor.execute('''
INSERT INTO CLASS (ID, NAME, STANDARDS, HOBBY, MARKS) VALUES
(1, 'Ananya Sharma', '10th', 'Painting', 92),
(2, 'Rohan Verma', '9th', 'Cricket', 78),
(3, 'Priya Singh', '10th', 'Reading', 85),
(4, 'Amit Kumar', '8th', 'Cycling', 74),
(5, 'Neha Patel', '9th', 'Dancing', 88),
(6, 'Arjun Mehta', '10th', 'Chess', 95),
(7, 'Isha Gupta', '8th', 'Singing', 81),
(8, 'Vikram Rao', '9th', 'Football', 69),
(9, 'Kavya Joshi', '10th', 'Sketching', 90),
(10, 'Devansh Nair', '8th', 'Coding', 99)
''')

conn.commit()

# Select data
cursor.execute("SELECT * FROM CLASS;")
data = cursor.fetchall()
print(data)


conn.close()
