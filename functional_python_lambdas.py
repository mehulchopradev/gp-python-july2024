# lambda expressions / lambda functions
# Pre requisite : lower order function must have only one statement

nos = [5, 4, 3, 6, 5, 8, 9, 10, 1]

'''
Build a new python list consisting of even numbers more than 2 from the nos list
Print the new python list -- filtering
Without using for comprehensions. should be functional
'''
print('**** evens more than 2 ****')

# filter -> higher order function
l1 = list(filter(lambda element: element % 2 == 0 and element > 2, nos))
print(l1)

'''
Build a new list consisting of students with 10 marks or less than 5
print the new python list -- filtering
without for comprehensons
functionally
'''
print('***** 10s or less than 5 *****')
l2 = list(filter(lambda element: element == 10 or element < 5, nos))
print(l2)

'''
Build a new python list consisting of all elements from nos list but each element deducted by 1 -- mapping
'''
print('***** deducted by 1 *****')
l3 = list(map(lambda element: element - 1, nos))
print(l3)


'''
Build a new python list consisting of odd numbers more than 3 from nos list and then squared up
-- filtering + mapping
'''
print('***** Odds more than 3 and then squared up *****')
a = filter(lambda element: element % 2 and element > 3, nos)
l4 = list(map(lambda element: element ** 2, a))
print(l4)