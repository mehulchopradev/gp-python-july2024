from com.globalpayex.college.student import Student

students = {
  10: Student('mehul', 'm', 10, 93),
  5: Student('jane', 'f', 5, 78),
  23: Student('rahul', 'm', 23, 45),
  16: Student('rock', 'm', 16, 90)
}

roll = int(input('enter roll: '))

if roll in students:
  print(students[roll].get_details())
else:
  print('not found')