import school

student_dict = {}

jason = school.Student(student_id=1, name='Jason', age=19, score=10)

student_dict[1] = jason

amy = school.Student(student_id=2, name='Amy', age=15, score=20)

student_dict[2] = amy

yin = school.Student(student_id=3, name='Yin', age=45, score=30)

student_dict[3] = yin

direct = int(input('What is your student ID?'))

if direct not in student_dict:
        print('This student ID cannot be found.')

else:
        student_dict.get(direct).print()