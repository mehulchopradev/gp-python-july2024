full_name = 'mehul chopra'
print(type(full_name)) # `str`

msg = 'good morning'

# indexing
print(full_name[0])
print(full_name[4])
print(full_name[-1]) # last
print(full_name[-3]) # third last

# substring
fname = full_name[0:5] # endindex is exclusive
print(fname)
lname = full_name[6:] # endindex is assumed to be the end of the string
print(lname)
fname = full_name[:5] # start index is assumed to be 0
print(fname)

# looping
for c in full_name:
  print(c)

# object oriented methods
cap = full_name.capitalize()
print(cap)
print(full_name)

print(full_name.title())
print(full_name.upper())

print(msg.startswith('good'))
print(msg.endswith('night'))

print(msg.replace('morning', 'night'))
print(msg.find('mor')) # 5
print(msg.find('bad')) # -1 Not found

student_data = '        mehul,m,10,90                           '
ss = student_data.strip()
print(student_data)
print(ss)

greeting = 'hello to all. hello world.'
print(greeting.count('hello'))

age = '37'
print(age.isnumeric())
age = 'three seven'
print(age.isnumeric())
print('mehul'.isalpha())



# extras
print(len(full_name))