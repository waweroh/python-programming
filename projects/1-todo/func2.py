FILEPATH = 'todofile.txt'

def read_todos(filepath=FILEPATH ):
  with open(filepath, 'r') as file:
    todos_local = file.readlines()
  return todos_local

def write_todo( todo_arg,filepath=FILEPATH ):
  with open(filepath, 'w') as file:
    file.writelines(todo_arg)

print(__name__)  #__main__

if __name__ == '__main__':
  print('implementing functions folder')