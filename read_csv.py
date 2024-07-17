from csv import reader, DictReader, DictWriter
from pathlib import Path

path = Path('data/students.csv')
dest_path = Path('data/students_projected.csv')

with open(file=path) as file:
  with open(file=dest_path, mode='w') as fw:
    student_writer = DictWriter(fw, fieldnames=['Name', 'Roll'])
    student_writer.writeheader()

    ''' student_reader = reader(file)
    for line in student_reader:
      print(line) '''
    student_reader = DictReader(file)
    for student in student_reader:
      student_writer.writerow({'Name': student['Name'].upper(), 'Roll': student['Roll']})