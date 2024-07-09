from com.globalpayex.college.student import Student

s1 = Student()
s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90

s2 = Student()
s2.name = 'jane'
s2.gender = 'f'
s2.roll = 14
s2.marks = 68

print(type(s1)) # Student
print(type(s2)) # Student

print(s1.name)
print(s2.name)
print(s1.gender)
print(s2.gender)