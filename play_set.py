fruits = {'apple', 'banana', 'chickoo', 'apple', 'rasberry', 'banana'}
print(type(fruits))
print(fruits)

# empty set
# es = {} # treat it as a dictionary
es = set()
print(type(es))
print(es)

# add elements to the set
fruits.add('mango')
fruits.add('mango') # silently ignored and will not be added to the set
print(fruits)

# remove element from the set
fruits.remove('apple')
print(fruits)

# iteration
for fruit in fruits:
  print(fruit.title())

# indexing
# print(fruits[0]) # since unordered data structure, it does not have indexing!

# Mathematical set operations
ma = [1, 3, 5]
mb = [3, 5, 9, 8]

# find out the common set of marks scored across the divisions
mas = set(ma)
mbs = set(mb)
l1 = list(mas & mbs) # intersection between the two sets
print(l1)

# find out the unique set of marks that were scored in division a
l2 = list(mas - mbs)
print(l2)

# find out the unique set of marks that were scored in division b
l3 = list(mbs - mas)
print(l3)

# find out the union of the two divisions
l4 = list(mas | mbs)
print(l4)