# user_prompt = 'enter to do item: '
# user_text = input(user_prompt)
# print (user_text)

# text = input('enter Todo: ')
# length = len(text)
# print ('the length of the title is : ', length)



# todos = [] #set empty list outside the loop

import main_func
import time # python module index

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is:', now)

while True:
  user_action = input('type add, edit,completed, show or exit: ')
  user_action = user_action.strip() #remove whitespaces

  
  if user_action.startswith('add'):
    todo = user_action[4:]

    #purpose is to load existing list of todos into memory before adding 
    #otherwise if we use empty list the tasks will disappear once we close the program.
    todos = main_func.get_todos()

    todos.append(todo + '\n')

    main_func.write_todo(todos)
    

  elif user_action.startswith('show') or  user_action.startswith('display'):
    
    todos = main_func.get_todos()
    # new_todos = []
    # for item in todos:
    #   new_item = item.strip('\n')
    #   new_todos.append(new_item):

    #new_todos = [item.strip('\n') for item in new_todos] #list comprehension
    

    for index,item in enumerate(todos):
      item = item.capitalize() #manipulate the item
      # index += 1 
      item = item.strip('\n') #stripping the new line
      row = f"{index + 1}-{item}"
      print(row) #print each to do in new line not list

  elif user_action.startswith('edit'): 
    try:
      number = int(user_action[5:]) #indexing num to edit
      number -= 1 #to access the true index ie. todo 2 is index 1

      todos = main_func.get_todos()

      existing_todo = todos[number]
      print (existing_todo) # display what to edit

      new_todo = input('Enter new todo: ') #new input
      todos[number] = new_todo + '\n' #replace

      main_func.write_todo(todos)
    except ValueError:
      print('Command is not valid.')
    except IndexError:
      print('Your index is not a valid index')
    continue

  elif user_action.startswith("completed"):
    try:
      number = int(user_action[10:])
      # number -= 1 
      todos = main_func.get_todos()

      done = todos[number - 1].strip('\n')
      print(f"task completed and removed: {done}") 
      todos.pop(number - 1)#pop index not done

      main_func.write_todo(todos)
    except IndexError:
      print('Enter a valid task number. Thank you.')
      continue
    
  elif user_action.startswith("exit"):
    break
  else:
    print("You entered an unknown command.")
  
print('bye !')
# print(dir(list))
# print(help(list.extend))
print(__name__) # main_func





