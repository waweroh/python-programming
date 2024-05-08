# for loop allows us to loop through anything that has items
for item in [1, 2, 3, 4, 0 ]:
  print(item)
print(item) #prints the last item in the list

# nested loops
for item in (1, 2, 3, 4, 0):
  for i in ['a', 'b', 'c']:
    print(item, i)
    # print(i) when item and i are printed separately they display differently

# Looping/iterating through iterables ie in this case a dictionary
#iterable is a collection of items
user = {
  'name': 'Moses',
  'age': 25,
  'can_swim': True
}
for item in user.items():
  print(item) #get the item k and v printed in a tuple

for k,v in user.items():
  print(k,v)# separating the items of a dicionary so no tuple

for item in user.keys():
  print(item)

for item in user.values():
  print(item)

#  counter exercise
my_list = [1,2,3,4,5,6,7,8,9,10]
counter =  0 # will give the summation 0 being the start of the counter
for item in my_list:
  #counter = 0 #putting counter inside loop will count n.o of items in the list
  counter += item
  #print(counter) # this will print as many time as there are items since it's in the loop
print(counter) # this will print the total of counter

# Range - is another iterable 
print (range(10)) # range(0, 10)

for number in range(0, 10, 2):#start,stop,stepover. We looped thru the range 10 times
  print('success') # print 0-9

# how to print numbers in a range
for number in range(0, 10):
  print(number)

for _ in range(10, 0, -2):
  print (list (range(10)))


#enumerate - works with iteratables
for i, char in enumerate('kindness'): #index, character of iterable
  print (i,char)

for i,char in enumerate(list(range(10))):
  print (i,char)
  if char == 5:
    print({f'the index of 5 is {i})'})
    

