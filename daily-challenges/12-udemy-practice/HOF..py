'''
functions that take other functions as arguments

'''

def greet():
  print('Hi')
def display(other_fun):
  print('This is display() function')
  other_fun() #here we are executing the function taken as a parameter
display(greet)