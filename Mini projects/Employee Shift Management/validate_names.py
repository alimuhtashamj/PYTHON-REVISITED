
def name_is_valid(employee_name):
    errors = []

    if employee_name.lower() == "done":
        return None

    if employee_name.strip() == "":
        errors.append("Empty")
    else:
        try:
            float(employee_name)
            errors.append("Numeric")
            return errors
        except ValueError:
            pass

    for ch in employee_name:
        if ch.isalpha() or ch.isspace():
            continue
        
    # if not isinstance(employee_name, str):
    #     errors.append('Not a string')
    #     print('This is not a valid name')
    #     return errors

        elif ch.isdigit():
            if "Contains digit" not in errors:
                errors.append("Contains digit")
                    # for ch in employee_name:
    #     if ch.isdigit():
    #         errors.append('Contains digit')
    #         print('Employee name contains a digit')
    #         return errors
    #     else:
    #        if not ch.isalnum():
    #            errors.append(employee_name)
    #            print('Employee name has a special character')
    #            return errors
    #        else:
    #            pass

        else:
            if "Contains special character" not in errors:
                errors.append("Contains special character")

    return errors

            
            