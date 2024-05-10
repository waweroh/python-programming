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

def sum(num1, num2):
  def another_fun(n1, n2):# function within a func
    return n1 + n2
  return another_fun (num1, num2)
total = sum(10,59)
print(total)