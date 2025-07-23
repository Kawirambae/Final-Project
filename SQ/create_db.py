import sqlite3
import os

# Get correct path to DB inside SQ
db_path = os.path.join(os.path.dirname(__file__), 'Sugarlevels.db')

# Connect and create table
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    medications TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database and table created successfully.")
