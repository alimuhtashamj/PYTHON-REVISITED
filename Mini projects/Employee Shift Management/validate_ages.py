def validate_age(age):
    try: 
        age = int(age)
    except ValueError:
        return 'Invalid age'
        
    upper_bound = 65 
    lower_bound = 18
    if age > upper_bound:
        return 'Invalid age'
    if age < lower_bound:
        return 'Invalid age'

    return age 