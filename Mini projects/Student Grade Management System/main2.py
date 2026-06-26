
def student_data():
    try:
        input_name = input('What is your name (in English )?')
        # str(input) is unnecessary because input already gives string in return
    except ValueError:
        print('Please input in valid format')
    try:
        input_roll_no = int(input('What is your roll number (in digits) ?'))
    except ValueError:
        print('Please input in valid format')
    try:
        input_marks = int(input('What are your Math Marks ( in digits)?'))
    except ValueError:
        print('Please input in valid format')
        
    student_dict = {}
    student_dict['Student Name'] = input_name
    student_dict['Roll Number'] = input_roll_no
    student_dict['Math Marks'] = input_marks
    return student_dict