
while True:
    employee_name = input('Add employee name').strip()
    errors = []
    try:
       employee_name = float(employee_name)
       errors.append(employee_name)
       print('This is a number, Please add valid name')
       continue
    except ValueError:
        pass
    if employee_name == '':
        errors.append('Empty')
        print('Add the employee name')    
        continue
    if employee_name.lower() == 'done':
        break
    else:
       print(employee_name)
       break
        
            
            