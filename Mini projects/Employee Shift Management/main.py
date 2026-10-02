from input import caller
from database import initialize_database, add_employee_db


def main():
    initialize_database()

    while True:
        employee = caller()

        if employee is None:
            break

        name, age = employee

        add_employee_db(name=name, age=age)


if __name__ == "__main__":
    main()