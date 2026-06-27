students = []
def main():
    while True:
        ask = input('Do you want to add another student?(y/n)')
        if ask == 'n':
            print('Okay')
            break
        else:
            if ask == 'y':
                user_input = student_data()
                students.append(user_input)
            
def student_data():    
        input_name = input('What is your name (in English )?')
        input_roll_no = int(input('What is your roll number (in digits) ?'))
        input_marks = int(input('What are your Math Marks ( in digits)?'))
        student_dict = {}
        student_dict['Student Name'] = input_name
        student_dict['Roll Number'] = input_roll_no
        student_dict['Math Marks'] = input_marks
        return student_dict

main()
print(students)