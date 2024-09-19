# todos = [] the list that stores todo list
while True:
  user_action = input('type add,show,edit,complete,exit: ')

  if 'add' in user_action:
    todo = input('enter todo task: ') + '\n'

    with open('todo2.txt', 'r') as file:
      todos = file.readlines()#opens the file in lines

    todos.append(todo)

    with open('todo2.txt', 'w') as file:
      file.writelines(todos)
      

  elif 'show' in user_action:
    with open('todo2.txt', 'r') as file:
      todos = file.readlines()

    for index,item in enumerate(todos):
      item = item.capitalize()
      item = item.strip('\n')
      row = f'{index + 1}-{item}' 
      print(row)
  
  elif 'edit' in user_action:
    number = int(input('enter todo task number: '))
    number -= 1

    with open('todo2.txt', 'r') as file:
      todos = file.readlines()

    changing_todo = todos[number]
    print(changing_todo)

    new_todo = input('enter modified todo task number: ')
    todos[number] = new_todo + '\n'

    with open ('todo2.txt', 'w') as file:
      file.writelines(todos)
    
  
  elif 'complete' in user_action:
    number = int(input('enter the index of the completed task: '))
    number -= 1

    with open('todo2.txt', 'r') as file:
      todos = file.readlines()

    completed_task = todos[number]
    print(f'task completed: {completed_task}')

    todos.pop(number)

    with open('todo2.txt', 'w') as file:
      file.writelines(todos)

  elif 'exit' in user_action:
    break

  else:
    print('You entered the wrong command')

print('goodday G')



