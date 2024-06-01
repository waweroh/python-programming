# default parameters
def say_hello(name='dashan', emojis='🙌'): # parameters
  print(f'Hello there {name}{emojis}')

# positional arguments
say_hello('moses','😊' )
say_hello('matthew','😊' )
say_hello('jane','😊' )

#keyword arguments
say_hello(name='gidi', emojis='😎')
say_hello()
say_hello(name='john')

# function within another function
def sum1(num1, num2):
  def another_fun(n1, n2):
    return n1 + n2
  return another_fun (num1, num2)
total = sum1(10,59)
print(total)

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age=0):
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

  return(age)   
checkDriverAge()
checkDriverAge(18)
checkDriverAge(35)
checkDriverAge(3)

# *args and **kwargs
# *args- Positional Arguments.When you use *args, it collects all the positional arguments into a tuple.
def super_func(*args):
  print(*args) #prints the arguments
  print(args) #prints the arguments in a tuple
  return sum(args) # returns the sum of the tuple

print(super_func(1,2,3,4,5)) #print sum

#kwargs- (Keyword Arguments.It collects all the keyword arguments into a dictionary where
          #the keys are the argument names and the values are the argument values.
def super_func(*args, **kwargs):
  print(*kwargs) #prints the arguments
  print(kwargs) #prints the arguments in a dictionary
  total = 0
  for items in kwargs.values():
    total += items #adds total=0 and the items in the dict being iterated over by the loop

  return sum(args) + total # returns the sum of the tuple and dictionary values

print(super_func(1,2,3,4,5, num1=5, num2=10)) #print sum

#Rules of passing parameters in order of priority: param, *args, default params, **kwargs

#Scope
a = 1 
def confusion():
  a=5
  return a

print(confusion())
print(a)
#1. start with local
#2. parent local/ the top function
#3. global ie  a = 1 whatever is the files scope

# Exercise highest even number
def highest_even(li):
  evens =[]
  

  for item in li:
    if item % 2 == 0:
      evens.append(item)
      print(evens)
      x = max(evens)

  return x #should be outside the for loop otherwise returns first item only

print(highest_even([20, 2, 11, 50, 13, 8, 9, 6, 7, 4]))

'''
FUNCTIONAL PROGRAMMING
Separation of concerns
Pure functions - For functional programming we need separation ie separating functions and data of concerns, hence 
                 the need for pure functions. They have 2 xristics
                 - given same input they return same output
                 - the function cannot be altered by outside code ie. maintains 
                   every thing within it's scope  

'''
#new_list = [] - having list outside func scope means can be altered in the func hence not pure func
def multiply_by_2(li):
  new_list = []
  for item in li:
    new_list.append(item*2)
  return new_list


print(multiply_by_2([2,4,6]))

'''
Map - The map() function in Python is used to apply a given function to each item of an
      iterable (such as a list, tuple, etc.) and return a map object (which is an iterator)

      $map specialty$
It helps in maintain pure functions which don't affect the scope outside them. In this case the 
iterable outside the func scope though used inside the function remains immutable and is callable.
'''
my_list = [1,2,3]
def multiply_by_3(item):
  return item*3

print(list(map(multiply_by_3,my_list)))
print(my_list)

'''
Filter - The filter() function is used to filter elements in an iterable based on a condition 
         provided by a function.

Also maintains original form of the iterable
filter names starting with A
'''
d_list = [4,6,8,5,7]
def multiply_by_4(item):
  return item*4

def only_odd(item):
  return item % 2 != 0

print(list(filter(only_odd, d_list)))
print(d_list)

'''
Zip - The zip() function in Python is used to combine multiple iterables (e.g., lists, tuples)
      into a single iterable of tuples. Each tuple contains elements from each of the input iterables,
      grouped by their position.
'''
d_list = [4,6,8,5,7]
my_list = [1,2,3]
your_list = [3,5,7]
def multiply_by_4(item):
  return item*4

def only_odd(item):
  return item % 2 != 0

print(list(zip( d_list, my_list, your_list)))
print(d_list)

'''
Reduce - functools.reduce(function, iterable[, initializer])

Apply function of two arguments cumulatively to the items of sequence, from left to right, so as to 
reduce the sequence to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates 
((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update
value from the sequence. If the optional initializer is present, it is placed before the items of the sequence 
in the calculation, and serves as a default when the sequence is empty. If initializer is not given and sequence 
contains only one item, the first item is returned.
'''
from functools import reduce
your_list = [3,5,7]

def multiply_by_4(item):
  return item*4

def only_odd(item):
  return item % 2 != 0

def accumulator(acc, item):
  print(acc, item)
  return acc + item

print(reduce(accumulator, your_list, 10 ))
print(your_list)

'''
lambda function - is an anonymous function that is syntactically restricted to
                  to a single expression.

    syntax: lambda param:action(param)

'''
your2_list = [3,5,7,6,8]
print(list(map(lambda item: item*2,your2_list)))
print(list(filter(lambda item: item % 2 !=0, your2_list)))
print(reduce(lambda acc, item: acc + item, your2_list,))

#squaring with lambda
print (list(map(lambda item: item**2, your2_list)))

#list sorting with lambda
#sort arranges in an order(alphabetic, ascending order )
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda pair: pair[1])
print(a)
print(your2_list)

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['nisi', 'babi', 'titi', 'carla']
def capital(item):
  a = item.capitalize()
  return a
print(list(map(capital, my_pets)))

  
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()
print(list(zip(my_numbers, my_strings)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def pass_mark(item):
  return item > 50
    
print(list(filter(pass_mark, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
  a = (acc + item)
  return a

print(reduce(accumulator,(my_numbers + scores)) )

'''
Decorator 
A decorator is essentially a higher-order function that takes another function as an argument and returns a new
function that typically extends or modifies the behavior of the original function.

'''
def my_decorator(func):
  def wrap_func():
    print('*********')
    func()
    print('*********')
  return wrap_func()

@my_decorator
def hello():
  print('helllooooo')

def bye():
  print('see ya latter')



