FILEPATH = 'file2.txt'

def read_file(filepath=FILEPATH):
  with open('file2.txt' , 'r') as file:
    local_todos = file.readlines()
  return local_todos

def write_file(todos_arg ,filepath=FILEPATH):
  with open('file2.txt', 'w') as file:
      file.writelines(todos_arg)

if __name__ == '__main__':
   print('you are implementing the functions folder')
