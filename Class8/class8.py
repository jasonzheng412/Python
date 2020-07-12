student_set = set()

student_set.add('Jason')

# print(student_set):

student_set.add('Jason')

student_set.add('Amy')

print(student_set)

student_set.remove('Jason')

if 'Jason' in student_set:
    print('I found Jason!')
else:
    print('I can\'t find Jason...')
