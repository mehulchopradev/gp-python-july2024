# 0 to n parameters
def next_gen_add(*nos):
  # print(nos) # tuple
  sum = 0
  for n in nos:
    sum = sum + n
  return sum

# positional arguments packing into a tuple
print(next_gen_add()) # 0
print(next_gen_add(4, 3)) # 7
print(next_gen_add(4, 3, 2, 5, 6)) # ..
print(next_gen_add(6, 5, 4, 3, 7, 8, 10, 3))



def perimeter(length, breadth):
  return 2 * (length + breadth)

measurements = (5, 3.5)
# print(perimeter(length=measurements[0], breadth=measurements[1]))
print(perimeter(*measurements)) # tuple unpacking to parameters



def area(**measurements):
  # print(measurements) # dict
  return measurements['length'] * measurements['breadth']

# print(area(5, 4)) # will not work
# keyword parameters packing
print(area(length=5, breadth=4))
print(area(breadth=2, length=4))


measurements_map = {'breadth': 5, 'length': 7}
# print(perimeter(length=measurements_map['length'], breadth=measurements_map['breadth']))
print(perimeter(**measurements_map))
