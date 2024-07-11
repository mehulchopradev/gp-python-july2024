books = {'B001': ('prog in java', 900, 1000), 'B002': ('c programming', 2000, 1500)}
print(type(books))
print(books)

# empty dict
et = {}

# indexing
print(books['B002'])

# add a new entry
books['B004'] = ('python programming', 2300, 900)
print(books)

# update an existing entry
books['B001'] = ('prog in groovy', 900, 1000)
print(books)

# remove an entry
del books['B002']
print(books)

# bifs
print(len(books))
print(len(et))

# iteration
''' for key in books:
  print('Book id: ' + key)
  print('Book title: ' + books[key][0]) '''

items = books.items()
for item in items:
  print('Book id: ' + item[0])
  print('Book title: ' + item[1][0])