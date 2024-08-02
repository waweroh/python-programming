# user_prompt = 'enter to do item: '
# user_text = input(user_prompt)
# print (user_text)

# text = input('enter Todo: ')
# length = len(text)
# print ('the length of the title is : ', length)



todos = [] #set empty list outside the loop

while True:
  user_action = input('type add, edit, show or exit: ')
  user_action = user_action.strip() #remove whitespaces

  match user_action:
    case 'add':
      todo = input('Enter a todo: ')
      todos.append(todo)
    case 'show'| 'display':
      for index,item in enumerate(todos):
        item = item.capitalize() #manipulate the item
        print(index,'.',item) #print each to do in new line not list

    case 'edit': #change input to num, access items on list, replace an item 
      number = int(input('Number to edit: ')) #indexing num to edit
      number -= 1
      existing_todo = todos[number]
      print (existing_todo) # display what to edit
      new_todo = input('Enter new todo: ') #new input
      todos[number] = new_todo #replace
    case 'exit':
      break
    case _:
      print("You entered an unknown command.")

print('bye !')




