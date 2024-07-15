'''
define a function calc_grade(marks) -> calculated grade
>= 70 -> A
>= 60 -> B
>= 40 -> C
< 40 -> F
> 100 or < 0 -> I

- take marks as user input
- call the above function and print the grade
'''

# Branching statements more than 2 branches : if / elif / elif /..... / else

# in python the scope of a variable is either the function or the entire file
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

marks = float(input('enter the marks scored: '))
# print('Hey you scored ' + calc_grade(marks) + ' grade')
print('Hey you scored {0} grade'.format(calc_grade(marks=marks)))