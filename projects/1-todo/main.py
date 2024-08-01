# user_prompt = 'enter to do item: '
# user_text = input(user_prompt)
# print (user_text)

# text = input('enter Todo: ')
# length = len(text)
# print ('the length of the title is : ', length)



todos = [] #set empty list outside the loop

while True:
  user_action = input('type add, show or exit: ')
  user_action = user_action.strip() #remove whitespaces

  match user_action:
    case 'add':
      todo = input('Enter a todo: ')
      todos.append(todo)
    case 'show':
      for item in todos:
        print(item) #print each to do in new line not list
    case 'exit':
      break

print('bye !')




