def name_is_valid(employee_name):

    if employee_name.lower() == "done":
        return None

    if employee_name.strip() == "":
        return "Empty"

    try:
        float(employee_name)
        return "Numeric"
    except ValueError:
        pass

    for ch in employee_name:
        if ch.isalpha() or ch.isspace():
            continue

        if ch.isdigit():
            return "Contains digit"

        return "Contains special character"
    return employee_name