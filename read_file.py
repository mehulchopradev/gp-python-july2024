# file operations
# reading from a file

file_path = 'enroll_students.py'
file = open(file=file_path)

# reading line by line from the file
''' for line in file:
  print(line.rstrip('\n')) '''

# read all lines from the file, at once
# avoid using this for larger files
''' lines = file.readlines()
for line in lines:
  print(line.rstrip('\n')) '''

# read all the contents of the file at once in a str
# avoid using this for larger files
contents = file.read()
print(type(contents)) # str
print(contents)

file.close()