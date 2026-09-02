import sqlite3
connection = sqlite3.connect('hr.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE employees(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);""")
cursor.execute("""INSERT INTO employees
               VALUES
               ('ali', 24),
               ('hassan', 24),
               ('zayn', 24);""")
connection.commit()