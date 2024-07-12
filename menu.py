'''
menu driven program

1. Even series
2. Odd series
3. Grader
4. Exit
Please enter ur choice: 1
Enter n: 8
0 2 4 6 8

1. Even series
2. Odd series
3. Grader
4. Exit
Please enter ur choice: 3
Enter marks: 78
You scored A grade

1. Even series
2. Odd series
3. Grader
4. Exit
Please enter ur choice: 2
Enter n: 5
1 3 5

1. Even series
2. Odd series
3. Grader
4. Exit
Please enter ur choice: 4
'''

# every python file is by default a `module`
# name of the module -> menu

# import a module
# import math_series
# import student_ops

# different name to the imported module
import com.globalpayex.lib.student_ops as so

# import functions from a module
from com.globalpayex.lib.math_series import even_series, odd_series # user defined modules
from math import factorial # built in module

while True:
  print('1. Even series', '2. Odd series', '3. Grader', '4. Factorial', '5. Exit', sep='\n')

  choice = int(input('Please enter ur choice: '))

  if choice == 5:
    break

  if choice == 1:
    n = int(input('enter n: '))
    # print(math_series.even_series(n))
    print(even_series(n))
  elif choice == 2:
    n = int(input('enter n: '))
    # print(math_series.odd_series(n))
    print(odd_series(n))
  elif choice == 3:
    marks = int(input('enter marks: '))
    # print('You scored ' + student_ops.calc_grade(marks) + ' grade')
    print('You scored ' + so.calc_grade(marks) + ' grade')
  elif choice == 4:
    n = int(input('enter n: '))
    print('Factorial of ' + str(n) + ' is ' + str(factorial(n)))
  else:
    print('Invalid choice')

