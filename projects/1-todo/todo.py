todos = []
while True:
  user_action = input('type add, show, complete or edit: ' )


  if 'add' in user_action:

    todo = input('enter todo task: ')
    todos.append(todo)
    # print(todos)

  if 'show' in user_action:
    for index, item in enumerate(todos):
      item = item.capitalize()
      row = f'{index + 1}-{item}'
      print (row)
  if 'edit' in user_action:
    number = int(input('Enter number to edit: '))
    number -= 1

    changing_todo = todos[number]
    print(changing_todo)

    new_todo = input('Enter new todo: ')
    todos[number] = new_todo
    print(new_todo)
