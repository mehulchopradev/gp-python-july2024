from datetime import datetime, date

current_datetime = datetime.now()
print(current_datetime)
print(type(current_datetime))

print(current_datetime.hour) # 24 hr clock
print(current_datetime.day)
print(current_datetime.month)
print(current_datetime.year)

current_hour = current_datetime.hour
if current_hour > 0 and current_hour < 12:
  print('good morning')
elif current_hour < 16:
  print('good afternoon')
else:
  print('good evening')

'''
define a function that takes ur birthday as a parameter and returns the age
'''

def calc_age(birthday):
  current_date = date.today()
  return current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

birthday = date(year=1986, month=11, day=25)
print(calc_age(birthday))