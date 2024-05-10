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
def sum(num1, num2):
  def another_fun(n1, n2):
    return n1 + n2
  return another_fun (num1, num2)
total = sum(10,59)
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




