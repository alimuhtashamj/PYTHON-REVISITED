from validate_names import name_is_valid
from validate_ages import validate_age



def caller():

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

            employee_data = {'name': name_result, 'age' : age}    
            break   
        return employee_data



