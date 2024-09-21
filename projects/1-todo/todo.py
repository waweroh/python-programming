# todos = []

import func2

while True:
  user_action = input('type add,show,edit,complete,exit: ')

  # if 'add' in user_action:
  #   todo = input('enter todo task: ') + '\n'
  if user_action.startswith('add'):
    todo = user_action[4:] + '\n'

    # with open('todofile.txt', 'r') as file:
    #   todos = file.readlines()
    todos = func2.read_todos()

    todos.append(todo) 

    # with open('todofile.txt', 'w') as file:
    #   file.writelines(todos)
    func2.write_todo(todos)
  
  # elif 'show' in user_action:
  elif user_action.startswith('show'):

    # with open('todofile.txt', 'r') as file:
    #   todos = file.readlines()
    todos = func2.read_todos()

    for index,item in enumerate(todos):
      index += 1
      item = item.capitalize()
      item = item.strip('\n')
      row = f'{index}-{item}'
      print(row)
  
  # elif 'edit' in user_action:
  elif user_action.startswith('edit'):
    try:
      number = int(user_action[5:])
      number -= 1

      # with open('todofile.txt', 'r') as file:
      #   todos = file.readlines()
      todos = func2.read_todos()

      changing_todo = todos[number]
      print(changing_todo)

      new_todo = input('enter modified todo: ')
      todos[number] = new_todo + '\n'

      # with open('todofile.txt', 'w') as file:
      #   file.writelines(todos)
      func2.write_todo(todos)
    except ValueError:
      print('command not valid enter an index')
      continue
    except IndexError:
      print('enter correct index')
    continue
  # elif 'complete' in user_action:
  elif user_action.startswith('complete'):
    try:
      number = int(user_action[9:])
      number -= 1

      # with open('todofile.txt', 'r') as file:
      #   todos = file.readlines()
      todos = func2.read_todos()

      completed_todo = todos[number]
      print(f'completed task:{completed_todo}')

      todos.pop(number)

      # with open('todofile.txt', 'w') as file:
      #   file.writelines(todos)
      func2.write_todo(todos)
    except ValueError:
      print('command not valid enter an index')
      continue
    except IndexError:
      print('enter correct index')
    continue

  elif user_action.startswith('exit'):
    break
  
  else:
    print('enter a valid command')

print('thank you G')