# user_prompt = 'enter to do item: '
# user_text = input(user_prompt)
# print (user_text)

# text = input('enter Todo: ')
# length = len(text)
# print ('the length of the title is : ', length)



# todos = [] #set empty list outside the loop

while True:
  user_action = input('type add, edit,completed, show or exit: ')
  user_action = user_action.strip() #remove whitespaces

  match user_action:
    case 'add':
      todo = input('Enter a todo: ') + '\n'

      file = open('todo.txt', 'r')
      todos = file.readlines()
      file.close()

      todos.append(todo)

      file = open('todo.txt', 'w')
      file.writelines(todos)
      file.close()

    case 'show'| 'display':
      file = open('todo.txt', 'r')
      todos = file.readlines()
      file.close()

      new_todos = []
      for item in todos:
        new_item = item.strip('\n')
        new_todos.append(new_item)
      

      for index,item in enumerate(new_todos):
        item = item.capitalize() #manipulate the item
        # index += 1 
        row = f"{index + 1}-{item}"
        print(row) #print each to do in new line not list

    case 'edit': #change input to num, access items on list, replace an item 
      number = int(input('Number to edit: ')) #indexing num to edit
      number -= 1
      existing_todo = todos[number]
      print (existing_todo) # display what to edit
      new_todo = input('Enter new todo: ') #new input
      todos[number] = new_todo #replace
    case 'completed':
      number = int(input('completed this task: '))
      # number -= 1 
      done = todos[number - 1]
      print(f"task completed: {done}") 
      todos.pop(number - 1) #pop index not done

      
      
    case 'exit':
      break
    case _:
      print("You entered an unknown command.")

print('bye !')
# print(dir(list))
# print(help(list.extend))




