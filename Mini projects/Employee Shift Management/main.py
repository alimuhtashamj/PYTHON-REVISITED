from input import caller
from database import initialize_database, add_employee_db, search_employee
from validate_inpt


def menu():
    print("\nEmployee Management System")
    print("1. Add employee")
    print("2. Search employee")
    print("3. Exit")

    choice = input("Select an option: ")

    return choice


def main():
    initialize_database()

    while True:
        choice = menu()

        if choice == "1":
            employee = caller()

            if employee is None:
                continue

            name, age = employee

            add_employee_db(name=name, age=age)

        elif choice == "2":
            ask_for_id = input('Add user id')
            validate_input_search
            pass

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()