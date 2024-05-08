i = 0
while i < 50:
  print(i)
  i += 1 # increment i until it equals 50
else:
  print('done')
  # break # break out of the while loop scope
  # to break out of the while turn condition false or break it


#for loop and while loop with the same result
my_toys_collection = [1,2,3,4]
for item in my_toys_collection:
  print(item)

i = 0 #Start at the first toy ie INDEX 0
while i < len(my_toys_collection):
  print(my_toys_collection[i])
  i += 1 #means you move to the next toy in the line increment

# # A good way to use loops
# #1.
# while True:
#   input('say something:')
#   break #otherwise it will continue asking question after the input.

#2.
while True:
  response = input('say something: ')
  if (response == 'yes'):
    break
# while loops are good when you don't know how many times the loop will execute
# pass, continue

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  for pixel in row:
    if (pixel == 1):
      print('*', end='')
    else:
      print(' ', end='')
  print()#prints new line in python after looping through the row 
