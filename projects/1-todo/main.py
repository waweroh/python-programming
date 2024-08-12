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

      with open('todo.txt', 'r') as file:
        todos = file.readlines()

      todos.append(todo)

      with open('todo.txt', 'w') as file:
        file.writelines(todos)
      

    case 'show'| 'display':
      with open('todo.txt', 'r') as file:
        todos = file.readlines()
      
      # new_todos = []
      # for item in todos:
      #   new_item = item.strip('\n')
      #   new_todos.append(new_item)

      #new_todos = [item.strip('\n') for item in new_todos] #list comprehension
      

      for index,item in enumerate(todos):
        item = item.capitalize() #manipulate the item
        # index += 1 
        item = item.strip('\n') #stripping the new line
        row = f"{index + 1}-{item}"
        print(row) #print each to do in new line not list

    case 'edit': #change input to num, access items on list, replace an item 
      number = int(input('Number to edit: ')) #indexing num to edit
      number -= 1

      with open('todo.txt', 'r') as file:
        todos = file.readlines()

      existing_todo = todos[number]
      print (existing_todo) # display what to edit

      new_todo = input('Enter new todo: ') #new input
      todos[number] = new_todo + '\n' #replace

      with open('todo.txt', 'w') as file:
        file.writelines(todos)

    case 'completed':
      number = int(input('completed this task: '))
      # number -= 1 
      with open('todo.txt', 'r') as file:
        todos = file.readlines()

      done = todos[number - 1].strip('\n')
      print(f"task completed and removed: {done}") 
      todos.pop(number - 1)#pop index not done

      with open('todo.txt','w') as file:
        file.writelines(todos)
      
    case 'exit':
      break
    case _:
      print("You entered an unknown command.")

print('bye !')
# print(dir(list))
# print(help(list.extend))




