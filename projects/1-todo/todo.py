todos = []
while True:
  user_action = input('type add, show, complete, edit or exit: ' )


  if 'add' in user_action:

    todo = input('enter todo task: ')
    todos.append(todo)
    # print(todos)

  elif 'show' in user_action:
    for index, item in enumerate(todos):
      item = item.capitalize()
      row = f'{index + 1}-{item}'
      print (row)

  elif 'edit' in user_action:
    number = int(input('Enter number to edit: '))
    number -= 1

    changing_todo = todos[number]
    print(changing_todo)

    new_todo = input('Enter new todo: ')
    todos[number] = new_todo
    print(new_todo)
  
  elif 'complete' in user_action:
    number = int(input('Enter number of task completed: '))
    number -=1 #  get index the done task

    done_todo = todos[number] #get done task by assigning variable the index
    print(f'task completed: {done_todo}')

    todos.pop(number) #remove it

  elif 'exit' in user_action:
    break
  
  else:
    print('You entered an unknown command')

print('bye G !')



