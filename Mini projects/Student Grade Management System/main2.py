students = []
def student_data():
    input_name = input('What is your name (in English )?')
    input_roll_no = int(input('What is your roll number (in digits) ?'))
    input_marks = int(input('What are your Math Marks ( in digits)?'))
      
    student_dict = {}
    student_dict['Student Name'] = input_name
    student_dict['Roll Number'] = input_roll_no
    student_dict['Math Marks'] = input_marks
    return student_dict

data = student_data()
students.append(data)
print(students)