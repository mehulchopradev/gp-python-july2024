el = []
print(type(el))

cars = ['audi', 'bmw', 'mercedes']

# indexing
print(cars[0])
print(cars[-1])
cars[0] = 'porshe'
print(cars)

# sublisting
nos = [5, 4, 3, 6, 5, 8, 9, 10, 1]
l1 = nos[0:4]
print(l1)

l2 = nos[-3:]
print(l2)

# membership
print('Bmw exists in list' + str('bmw' in cars))
print('Kia not in the list' + str('kia' not in cars))

# length
print(len(cars))
print(len(nos))
print('max marks scored is ' + str(max(nos)))
print('min marks scored is ' + str(min(nos)))

# iteration
for car in cars:
  print(car.capitalize())

# object oriented methods
cars.append('i10')
print(cars)
cars.extend(['i20', 'audi'])
print(cars)

print(cars.pop())
print(cars)
print(cars.pop())
print(cars)

cars.insert(0, 'audi')
print(cars)

print(cars.pop(2))
print(cars)

cars.remove('porshe')
print(cars)

print(nos.count(5))

nnos = nos.copy()
nnos.reverse()
print(nnos)
print(nos)

ma = [3, 5, 1]
mb = [10, 3, 2, 6]
m = ma + mb
print(m)

print(nos)
del nos[:4]
print(nos)

nos.sort(reverse=True)
print(nos)
