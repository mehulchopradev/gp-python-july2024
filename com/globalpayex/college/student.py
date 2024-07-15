# custom class
# specialized class
# sub class
# child class
from com.globalpayex.college.college_user import CollegeUser
class Student(CollegeUser):

  # constructor
  def __init__(self, name, gender, roll, marks):
    super().__init__(name, gender)
    # Internally
    # CollegeUser | __init__(self, name, gender)
    
    self.roll = roll
    self.marks = marks

    # Implicitly
    # return self

  # instance methods

  # method overriding
  def get_details(self):
    ''' return 'Name: ' + self.name + '\nGender: ' + self.gender\
    + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks) '''
    # return 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(self.name, self.gender, self.roll, self.marks)
    return 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'\
      .format(name=self.name, gender=self.gender, roll=self.roll, marks=self.marks)
  
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