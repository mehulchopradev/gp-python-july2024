from com.globalpayex.college.college_user import CollegeUser
class Professor(CollegeUser):

  def __init__(self, name, gender, subjects=[]):
    super().__init__(name, gender)
    # Internally
    # CollegeUser | __init__(self, name, gender)

    self.subjects = subjects