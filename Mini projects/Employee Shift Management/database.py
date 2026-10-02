import sqlite3


DATABASE = "hr.db"


def initialize_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        );
    """)

    connection.commit()
    connection.close()


def add_employee_db(name, age):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees (name, age)
        VALUES (?, ?)
    """, (name, age))

    connection.commit()
    connection.close()
    
def search_employee(employee_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, age
        FROM employees
        WHERE id = ?
        """,
        (employee_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result