# user_prompt = 'enter to do item: '
# user_text = input(user_prompt)
# print (user_text)

# text = input('enter Todo: ')
# length = len(text)
# print ('the length of the title is : ', length)

user_prompt = 'enter to do item: '

todos = [] #set empty list outside the loo[]
while True:
  todo = input(user_prompt)
  todos.append(todo) #method
  print (todos)