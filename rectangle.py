def perimeter_rectangle(length=3, breadth=2):
  return 2 * (length + breadth)

def area_rectangle(length, breadth):
  return length * breadth

def statistics(length, breadth):
  p = perimeter_rectangle(length, breadth)
  a = area_rectangle(length, breadth)

  return (p, a)

'''
input() always returns user input as a `str`
data type
'''
''' l = float(input('enter the length: '))
b = float(input('enter breadth: ')) '''

# p = perimeter_rectangle(l, b)
# a = area_rectangle(l, b)

# built in functions
# print('Perimeter is ' + str(p)) # int -> str 18 -> '18'
# print('Area is ' + str(a))

# function overloading
''' print(perimeter_rectangle(5)) # breadth default value 2
print(perimeter_rectangle(7)) # breadth default value 2
print(perimeter_rectangle(3)) # breadth default value 2
 
print(perimeter_rectangle()) '''

''' t = statistics(l, b)
print('Perimeter is ' + str(t[0]))
print('Area is ' + str(t[1])) '''