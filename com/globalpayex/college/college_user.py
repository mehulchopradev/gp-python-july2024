# generalized class
# super class
# parent class

# every class in python implicitly inherits from the `object` class in python
class CollegeUser(object):

  def __init__(self, name, gender):
    # self --> Student object (5004), Professor object (6003), or any subclass object of CollegeUser
    self.name = name
    self.gender = gender

  def get_details(self):
    return 'Name: '+ self.name + '\nGender: ' + self.gender
  
  def __str__(self):
    return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)