n = 45

# odd numbers till n
# 0 - n
  # check whether the number is odd or no
  # if odd, print the number

# Looping statements

# while loop (not preferred)
''' i = 0
while i <= n:
  if i % 2:
    print(i)
  i = i + 1
'''

# for loop (preferred)
'''
for v in <<sequence of elements>>:
  I1
  I2
  I3
'''
# 0 - n
  # check whether the number is odd or no
  # if odd, print the number
# range of numbers from 0 to n
''' for i in range(0, n + 1): # n + 1 ? because end index in range() is always exclusive
  if i % 2:
    print(i)
'''

# odd nunbers from 0 to n : but without an if condition
for i in range(1, n + 1, 2): # step size is 2
  print(i)