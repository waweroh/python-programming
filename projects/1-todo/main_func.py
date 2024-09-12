FILEPATH = 'todo.txt' # the constants in the module being imported

def get_todos(filepath=FILEPATH):
  with open(filepath, 'r') as file:
    todos_local = file.readlines()
  return todos_local

def write_todo(todos_arg,filepath=FILEPATH):
  with open(filepath, 'w') as file:
    file.writelines(todos_arg)

print(__name__)  # __main__

# this code will only be executed in the main file not where this code is imported to
if __name__ == '__main__': 
  print ('implementing functions folder')
  print (get_todos())