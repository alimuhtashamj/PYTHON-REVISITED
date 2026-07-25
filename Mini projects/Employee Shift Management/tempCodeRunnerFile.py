from validate_names import name_is_valid

employee_data = []
def caller():
    while True:
        employee= {}
        add_employee_name = input("Add employee's name")
        
        employee['employee name'] = add_employee_name
        results = name_is_valid(employee['employee name'])
        employee_data.append(employee)
        if results is None:
            break
        elif isinstance(results, list):
            employee['errors'] = results
        else:
            continue
     

output = caller()
print(output)
