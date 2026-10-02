def validate_input(emp_id):
    try: 
        emp_id = int(emp_id)
    except ValueError:
        return 'Invalid id'
    if id < 0:
        return 'Invalid id'

    return emp_id