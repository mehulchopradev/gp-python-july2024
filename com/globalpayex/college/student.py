# custom class
class Student:

  # constructor
  def __init__(self, name, gender, roll, marks):
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    # Implicitly
    # return self

  # instance methods
  def get_details(self):
    # self -> s1, s2, s100,, current Student object
    return 'Name: ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + str(self.roll)\
        + '\nMarks: ' + str(self.marks)
  
  def calculate_grade(self):
    marks = self.marks
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