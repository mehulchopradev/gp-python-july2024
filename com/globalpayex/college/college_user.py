# generalized class
# super class
# parent class
class CollegeUser:

  def __init__(self, name, gender):
    # self --> Student object (5004), Professor object (6003), or any subclass object of CollegeUser
    self.name = name
    self.gender = gender

  def get_details(self):
    return 'Name: '+ self.name + '\nGender: ' + self.gender