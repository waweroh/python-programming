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

