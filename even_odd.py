'''
- define a function that takes n as parameter and return "even" or "odd"
- take number as user input
- call the above function
- print the output
'''

# Branching statements - if / else
''' def evenodd(n):
  if n % 2:
    return "odd"
  else:
    return "even" '''

# Branching statements - if / else comprehensions
# Pre requisite - both branches must have only 1 instruction to execute
def evenodd(n):
  return "odd" if n % 2 else "even"
  
''' n = int(input('enter n: '))
print(evenodd(n)) '''