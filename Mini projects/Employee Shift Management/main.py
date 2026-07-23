from validate_names import name_is_valid

employee = {}
def caller():
    add_employee_name = input("Add employee's name")
    
    employee['employee name'] = add_employee_name
    results = name_is_valid(employee['employee name'])
    if results is None:
        return 
    elif isinstance(results, list):
        print(results)
        return 
    else:
       return results

caller()
