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




