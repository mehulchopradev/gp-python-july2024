from pathlib import Path
from json import loads, dumps

file_path = Path('data/students.json')
dest_path = Path('data/students_projected.json')

with open(file=file_path) as file:
  content = file.read()
  obj = loads(content)
  
  obj2 = [{'name': student['name'].upper(), 'gender': student['gender']} for student in obj]
  write_content = dumps(obj2)

  with open(file=dest_path, mode='w') as fd:
    fd.write(write_content)