b1 = ('prog in c', 1000, 980)
print(type(b1))
print(b1)

# empty tuple
et = ()
print(type(et))

# tuple with only 1 element
b2 = ('java programming',)
print(type(b2))
print(b2)

# indexing
print(b1[0])
print(b1[-1])

# b1[0] = 'python prog' # cannot do as tuple is immutable

# subtuple
t = b1[0:2]
print(t)

# bifs
print(len(b1))
print(len(b2))

# iteration
for element in b1:
  print(element)