""" 
dictionaries are used to store sets of data ie keys and values
{key: value} - used to store key and value
[] print the values of the dictionary
print items to get both keys and values

"""
x = {"A", "B", "C"}
y = "b" in x
print (y)

x = {0:4, 1:8, 2:16, 3:32}
y = 1 in x 
print (y)

x = {0:4, 1:8, 2:16, 3:32}
print (x[1])

#Creating dictionaries
dict1 = {'color': 'blue', 'shape': 'square', 'volume':40, 'weight':120}
dict2 = {'color': 'red', 'edges': 4, 'perimeter':15}

#Creating new pairs and updating old ones
dict1['area'] = 25 #{'color': 'blue', 'shape': 'square', 'volume': 40, 'area': 25}
dict2['perimeter'] = 20 #{'color': 'red', 'edges': 4, 'perimeter': 20}

#Accessing values through keys
print(dict1['area'])

#You can also use get, which doesn't cause an exception when the key is not found
dict1.get('false_key') #returns None
dict1.get('false_key', "key not found") #returns the custom message that you wrote 

#Deleting pairs
dict1.pop('volume')

#Merging two dictionaries
dict1.update(dict2) #if a key exists in both, it takes the value of the second dict
dict1 #{'color': 'red', 'shape': 'square', 'area': 25, 'edges': 4, 'perimeter': 20}

#Getting only the values, keys or both (can be used in loops)
dict1.values() #dict_values(['red', 'square', 25, 4, 20])
dict1.keys() #dict_keys(['color', 'shape', 'area', 'edges', 'perimeter'])
print(dict1.items())
#dict_items([('color', 'red'), ('shape', 'square'), ('area', 25), ('edges', 4), ('perimeter', 20)])