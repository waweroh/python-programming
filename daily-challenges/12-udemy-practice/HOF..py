'''
functions that take other functions as arguments

'''

def greet_louder(name):
  print(f'Hi {name.upper()}')
def greet_softer(name):
  print(f'Hi {name.lower()}')

def hello(other_fun, name):
  print('This is display() function')
  return lambda: other_fun(name) #here we are executing the function taken as a parameter
greet_1 = hello(greet_louder,'Moses')
greet_2 = hello(greet_softer,'Sophie')

greet_1()
greet_2()


def hello(name):
  print('hello has been executed')
  def greet():
    print('Hi Jenny')
  def welcome():
      print('you are welcome sana')
  if name == "Jenny":
     return greet
  else:
     return welcome
new_func = hello('Jenny')
new_func2 = hello('John')
new_func()
new_func2()
  