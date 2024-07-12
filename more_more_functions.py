from math import pi

name = 'mehul chopra'

# creating a `function` object in the memory
# functions are treated as regular values like str, float, boolean, list
# a variable = the name of the function gets auto created in the current scope
def area_circle(radius):
  return pi * (radius ** 2)

print(type(name)) # class `str`
print(type(area_circle)) # class `function`

# area_circle ---> callable variable
# name ---> non callable variable

print(area_circle(radius=4)) # callable
# print(name()) # non callable


# a function can be defined inside another function in python
def abc(i):
  j = 10 # j (int) -> abc

  # pqr (function) -> abc
  def pqr():
    k = 2 # k (int) -> pqr
    # inner function can access the enclosing function variables
    return (i + j + k) ** 2
  
  print(pqr())

abc(2)


# a function can return another function python
def mno(t):
  x = 10 # x (int) -> mno

  # qtr (function) -> mno
  def qtr(y):
    '''
    inner function has continuous access to the enclosing environment variable values
    even when the enclosing function has returned -- Closures
    '''
    return (x + y) ** t
  
  return qtr

fu = mno(t=2) # fu (function) (callable)
print(fu(y=3))



# passing a function as a parameter to another function
# wer (function) --> file (callable)
def wer(fn):
  k = 5
  l = fn(k)
  return l + 20

# rty (function) --> file (callable)
def rty(i):
  j = 10
  return (i ** 2) + j

print(wer(rty)) # callback function