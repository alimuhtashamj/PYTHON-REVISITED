from validate_names import name_is_valid
from validate_ages import validate_age
employee_data = []


def caller():
    while True:
        employee = {}

        employee_name = input("Add employee's name: ")

        results = name_is_valid(employee_name)

        if results is None:
            break
        if results == "Empty":
            continue
        if results == "Numeric":
            continue
        if results == "Contains digit":
            continue
        if results == 'Contains special characters':
            continue
#continue here actually starts the loop all over again and doesnt
#let python append the name in the dictionary
    
        employee["name"] = employee_name
        age = input('Add employee age')
        age_validation = validate_age(age)
        if age_validation != 'Invalid age':
            employee["employee_age"] = age_validation

        employee_data.append(employee)

    return employee_data


employees = caller()

print("\nEmployee Records\n")

