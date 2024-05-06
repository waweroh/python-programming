# dictionary, hash-table, map, object
# key value pair
# scattered in memory
dictionary ={
  'a':1,
  'b':2,
  'c':3,
  'd':4,
}
print(dictionary['d'])

# We can have different iterables/ds within each other 
# dict
assets = {
  'a':[1,2,3,4],
  'b':'hi there',
  'c':False
}
print(assets['a'][2])

# list with other data structures in practice
my_list =[
  {
  'a':[1,2,3,4],
  'b':'hi there',
  'c':False
},
{
  'a':[4,5,6,7],
  'b':'hi ',
  'c':True
}
]
print(my_list[0]['a'][3])

# dict
  # 1.hold more information due to key value pair xristics
  # 2. They are unordered

# list
  # 1.holds less info.
  # 2.useful in ordered things

# keys must be a unique and immutable iterables the values can have any data structure
  #list is mutable

# using get dict method to find or add to the dictionary

user = {
  'basket':[1,2,3],
  'greeting':'hello world',
  'age':20
}
print (user.get('height',180))
print('age' in user.values())
print('age' in user.keys())
print( user.items())
print( user.pop('age'))
print( user.update({'age': 50}))

user2 = user.copy()
print(user.clear())
print(user2)

