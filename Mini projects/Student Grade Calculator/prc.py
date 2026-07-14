student = {
    "name": None ,
    "marks":[10,30,40,90],
    "bonus": 5 }
def validate_name(nama):
    if nama is None:
        print('Student Name not Found')
        return
    if len(nama) == 0:
        print('Please add the name') 
        return
    return nama 


def is_valid_bonus(value):
    if value<0 or value >100 : return {value},'is out of range (0-100), Please add value in range'
    return value 
    # return 0 <=value <=100



def are_marks_valid(score):
    
    result = {}
    keys = ['message', 'truthiness']
    result = result.fromkeys(keys)
    for value in score:
        if value < 0:
            print('Add score in positive numbers')
            result['message'] = 'Add score in positive numbers'
            result['truthiness'] = False
        if value > 100:
            print('Please add marks in range (0-100)')
            result['message'] = 'Please add marks in range (0-100)'
            result['truthiness'] = False
        else:
            return True
        return score


# def is_valid_name(check_name):
#     if len(check_name) == 0:
#         print('Please add the name')
#     else:
#         return check_name 
    
# is_valid_name(student['name'])

def validate_student(student):
    student_name = validate_fields(student['name'])
    marks = are_marks_valid(student['marks'])
    bonus = is_valid_bonus(student["bonus"])
    return student_name, marks, bonus

validate_student(student)