nos = [5, 4, 3, 6, 5, 8, 9, 10, 1]

'''
Build a new python list consisting of even numbers more than 2 from the nos list
Print the new python list -- filtering
Without using for comprehensions. should be functional
'''
print('**** evens more than 2 ****')

# lower order function
def evens_more_than_2(element):
  return element % 2 == 0 and element > 2

# filter -> higher order function
l1 = list(filter(evens_more_than_2, nos))
print(l1)

'''
Build a new list consisting of students with 10 marks or less than 5
print the new python list -- filtering
without for comprehensons
functionally
'''
print('***** 10s or less than 5 *****')
def tens_or_less_than_5(element):
  return element == 10 or element < 5
l2 = list(filter(tens_or_less_than_5, nos))
print(l2)

'''
Build a new python list consisting of all elements from nos list but each element deducted by 1 -- mapping
'''
print('***** deducted by 1 *****')
def deduct_by_1(element):
  return element - 1
l3 = list(map(deduct_by_1, nos))
print(l3)


'''
Build a new python list consisting of odd numbers more than 3 from nos list and then squared up
-- filtering + mapping
'''
# 2 lower order functions
def odds_more_than_3(element):
  return element > 3 and element % 2
def square(element):
  return element ** 2

# 2 higher order functions -- data pipeline
a = filter(odds_more_than_3, nos)
l4 = list(map(square, a))
print(l4)