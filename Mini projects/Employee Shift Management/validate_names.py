name = 'Ali!'
def name_is_valid(employee_name):
    errors = []
    # if not isinstance(employee_name, str):
    #     errors.append('Not a string')
    #     print('This is not a valid name')
    #     return errors
    if employee_name.lower() == 'done':
        return
    if employee_name.strip() == '':
        errors.append('Empty')
        print('Add the employee name')
        return errors

    # check if the string is a number
    try:
        float(employee_name)
        errors.append('Numeric')
        print('This is a number, please add a valid name')
        return errors
    except ValueError:
        pass
    

    for ch in employee_name:
        if ch.isdigit():
            errors.append('Contains digit')
            print('Employee name contains a digit')
            return errors
        else:
           if not ch.isalnum():
               errors.append(employee_name)
               print('Employee name has a special character')
               return errors
           else:
               pass
            

    print(employee_name)
    return employee_name, errors

name_is_valid(name)
   
        
            
            