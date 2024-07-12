from com.globalpayex.lib.student_ops import calc_grade, get_details

# Procedural programming

# print(get_details('mehul', 'm', 10, 90))
print(get_details(name='mehul', gender='m', roll=10, marks=90))
print(get_details(gender='f', marks=56, name='jane', roll=13))

print(calc_grade(marks=90))