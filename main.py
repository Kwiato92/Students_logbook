Students_logbook = True
button = ['1', '2', '3', '4', '5', '6']
Students_list = {
    1: 'Piotr Zyla',
    2: 'Kamil Stoch',
    3: 'Klemens Muranka',
    4: 'Gregor Schlierenzauer',
    5: 'Maciej Kot'
}
Students_grades_maths = {
    1: [2],
    2: [6],
    3: [4],
    4: [4],
    5: [5]
}

while Students_logbook:
    print("""Please select:
    Student List: 1
    Student Grades: 2
    Add Grade: 3
    Student Average Grades: 4
    Add Student: 5
    Delete Student: 6""")
    action = input()

    if action == button[0]:
        for key, value in Students_list.items():
            print(f'{key}, {value}')
    elif action == button[1]:
        for key, value in Students_grades_maths.items():
            print(f'{Students_list[key]} - Maths Grades: {", ".join(map(str, value))}')
    elif action == button[2]:
        print('Choose a student number')
        student_number = int(input())
        if student_number in Students_grades_maths:
            print(Students_list[student_number])
            print('Do you want to add a grade? (yes/no)')
            add_grade = input()
            if add_grade.lower() == 'yes':
                print('Enter the grade:')
                grade = float(input())
                Students_grades_maths[student_number].append(grade)
        else:
            print('Invalid student number')
    elif action == button[3]:
        print('Choose a student number')
        student_number = int(input())
        if student_number in Students_grades_maths:
            grades = Students_grades_maths[student_number]
            if len(grades) > 0:
                average = sum(grades) / len(grades)
                print(f'Average Grades for {Students_list[student_number]}: {average}')
            else:
                print(f'No grades available for {Students_list[student_number]}')
        else:
            print('Invalid student number')
    elif action == button[4]:
        print('Enter the name of the new student:')
        new_student_name = input()
        new_student_number = max(Students_list.keys()) + 1
        Students_list[new_student_number] = new_student_name
        Students_grades_maths[new_student_number] = []
        print(f'Student {new_student_name} added with number {new_student_number}')
    elif action == button[5]:
        print('Choose a student number to delete')
        student_number = int(input())
        if student_number in Students_list:
            deleted_name = Students_list.pop(student_number)
            deleted_grades = Students_grades_maths.pop(student_number)
            print(f'Student {deleted_name} (number {student_number}) has been deleted.')
        else:
            print('Invalid student number')
