from validate_names import name_is_valid

employee = {}
def caller():
    while True:
        add_employee_name = input("Add employee's name")
        
        employee['employee name'] = add_employee_name
        results = name_is_valid(employee['employee name'])
        if results is None:
            break
        elif isinstance(results, list):
            print(results)
        else:
         continue
     

output = caller()
print(output)
