from com.globalpayex.college.student import Student

'''
- create a list of 4 Student objects
- take roll number of student to search as user input
- find the Student object from the list on the basis of the entered roll number
- if found, display all the details of the Student
- if not found, display "Not found"
'''

students = [
  Student('mehul', 'm', 10, 93),
  Student('jane', 'f', 5, 78),
  Student('rahul', 'm', 23, 45),
  Student('rock', 'm', 16, 90)
]

roll = int(input('enter roll: '))

''' found = False
for student in students:
  if student.roll == roll:
    print(student.get_details())
    found = True
    break

if not found:
  print('not found!') '''

# for - else
for student in students:
  if student.roll == roll:
    print(student.get_details())
    break
else:
  # will execute when the corresponding for block has been completely exhausted in its iterations (without a break)
  print('not found')