from validate_names import name_is_valid

employee_data = []


def caller():
    while True:
        employee = {}

        employee_name = input("Add employee's name: ")

        results = name_is_valid(employee_name)

        if results is None:
            break

        employee["name"] = employee_name
        employee["errors"] = results

        employee_data.append(employee)

    return employee_data


employees = caller()

print("\nEmployee Records\n")

for employee in employees:
    print(employee)