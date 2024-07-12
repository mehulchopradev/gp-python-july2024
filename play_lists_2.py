nos = [5, 4, 3, 6, 5, 8, 9, 10, 1]

'''
Build a new python list consisting of even numbers more than 2 from the nos list
Print the new python list -- filtering
'''
''' l1 = []
for n in nos:
  if n % 2 == 0 and n > 2:
    l1.append(n) '''

# pre requisite --- needing a new list
# for comprehensions
print('**** evens more than 2 ****')
l1 = [n for n in nos if n % 2 == 0 and n > 2]
print(l1)

'''
Build a new python list consisting of students who have scored 10 marks or less than 5 marks -- filtering
'''
print('**** 10 or less than 5 marks ****')
l2 = [n for n in nos if n == 10 or n < 5]
print(l2)

'''
Build a new python list consisting of all elements from nos list but each element deducted by 1 -- mapping
'''
print('**** Deducted by 1 ****')
l3 = [n - 1 for n in nos]
print(l3)

'''
Build a new python list consisting of odd numbers more than 3 from nos list and then squared up
-- filtering + mapping
'''
print('**** odds more than 3, squared up ****')
l4 = [n ** 2 for n in nos if n % 2 and n > 3]
print(l4)