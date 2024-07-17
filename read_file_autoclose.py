# file operations
# reading from a file
from pathlib import Path

file_path = input('enter the file path from where u want to read: ')
path = Path(file_path)

if not path.exists():
  print('hey, path provided by you does not exist!')
elif path.is_dir():
  print('hey, please pass in file path and not directory path')
else:
  with open(file=file_path) as file:
    for line in file:
      print(line.rstrip('\n'))

  # once outside the `with` block, the file object will be autoclosed