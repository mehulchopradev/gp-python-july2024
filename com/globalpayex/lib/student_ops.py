# Module -> student_ops

def calc_grade(marks):
  if marks > 100 or marks < 0:
    grade = 'I'
  elif marks >= 70:
    grade = 'A'
  elif marks >= 60:
    grade = 'B'
  elif marks >= 40:
    grade = 'C'
  else:
    grade = 'F'

  return grade

'''
Name: mehul\n
Gender: m
Roll: 10
Marks: 90
'''
def get_details(name, gender, roll, marks):
  return 'Name: ' + name + '\nGender: ' + gender + '\nRoll: ' + str(roll) + '\nMarks: ' + str(marks)