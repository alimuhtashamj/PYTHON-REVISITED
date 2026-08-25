from caller_trial import caller
from manager import Manager


def main():
    manager = Manager()
    while True:
        employee = caller()
        if employee is None:
            break
        manager.add_employee(employee)

    # Print stored employees after input ends
    if manager.employee_data:
        print("Stored employee info:")
        for emp_id, emp in manager.employee_data.items():
            print(f"ID: {emp_id}, Name: {emp['name']}, Age: {emp['age']}")
    else:
        print("No employees were added.")


if __name__ == "__main__":
    main()
