from validate_names import name_is_valid
from validate_ages import validate_age

employee_data = {}


def caller():
    if not employee_data:
        employee_id = 1000
    else:    
        largest_id  = max(employee_data)
        employee_id = largest_id + 1
    while True:
        employee_name = input("Add employee's name: ")

        name_result = name_is_valid(employee_name)

        if name_result is None:
            break

        if name_result != employee_name:
            print(f"Invalid name: {name_result}")
            continue

        while True:
            age = input("Add employee age: ")

            age_result = validate_age(age)

            if age_result == "Invalid age":
                print("Invalid age. Please enter an age between 18 and 65.")
                continue
        
            employee = {
                 "name": name_result,
                 "employee_age": age_result
             }   
            employee_data[employee_id] = employee 
            employee_id+= 1
            break
        
        


    return employee_data


employees = caller()
print(employees)

