# # default parameters
# def say_hello(name='dashan', emojis='🙌'): # parameters
#   print(f'Hello there {name}{emojis}')

# # positional arguments
# say_hello('moses','😊' )
# say_hello('matthew','😊' )
# say_hello('jane','😊' )

# #keyword arguments
# say_hello(name='gidi', emojis='😎')
# say_hello()
# say_hello(name='john')

# # function within another function
# def sum(num1, num2):
#   def another_fun(n1, n2):
#     return n1 + n2
#   return another_fun (num1, num2)
# total = sum(10,59)
# print(total)

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


