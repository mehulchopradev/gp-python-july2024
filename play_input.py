print('Program starts')

# Exceptions
try:
  n = int(input('enter n: '))
except ValueError:
  print('please enter numeric values only')
else:
  # will execute if there has been no exception (error) in the corresponding try block
  print('odd') if n % 2 else print('even')

print('Program ends')


# try - except
# try - except - except - *
# try - except - else