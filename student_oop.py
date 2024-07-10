from com.globalpayex.college.student import Student

# range(2, 10, 2)

# s1 = Student()
# Internally
# 1. at some random address in the ram (4003) object is created
# 2. Student() ----> Student | __init__(4003) ----> s1

''' s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90 '''

s1 = Student('mehul', 'm', 10, 90)
# Internally
# 1. at some random address in the ram (5004) object is created
# 2. Student('mehul', 'm', 10, 90) ---> Student | __init__(5004, 'mehul', 'm', 10, 90)

# s2 = Student()
# Internally
# 1. at some random address in the ram (5003) object is created
# 2. Student() ----> Student | __init__(5003) ---> s2

''' s2.name = 'jane'
s2.gender = 'f'
s2.roll = 14
s2.marks = 68 '''

s2 = Student('jane', 'f', 14, 68)

# print(type(s1)) # Student
# print(type(s2)) # Student

# print(s1.name)
# print(s2.name)
# print(s1.gender)
# print(s2.gender)

print(s1.get_details())
# Internally
# s1.get_details() ----> Student| get_details(s1)


print(s2.get_details())
# Internally
# s2.get_details() ---> Student | get_details(s2)

print(s1.calculate_grade()) # Student | calculate_grade(s1)

print(s2.calculate_grade()) # Student | calculate_grade(s2)