def validate_input(emp_id):
    try: 
        emp_id = int(emp_id)
    except ValueError:
        return 'Invalid id'
    if emp_id < 0:
        print('Invalid ID')
        return 'Invalid id'

    return emp_id