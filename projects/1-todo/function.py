def greet(message): # parameter
  new_message = message.capitalize()
  print('Hello')
  return new_message

user_entry = input('what greeting do you want ')
greeting = greet(user_entry) #function takes argument
print(greeting)

# function must have a return value