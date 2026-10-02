import sqlite3
DATABASE = "hr.db"
def initialize_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
        id INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );""")
    connection.commit()
    connection.close()
def add_employee_db():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO employees(name,age)
                VALUES
                ('ali', 24),
                ('hassan', 24),
                ('zayn', 24);""")
    connection.commit()
    connection.close()