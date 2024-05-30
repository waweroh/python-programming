basket = [1,2,3,4,5,5,6,8,10,11,11]

#List has the advantage of method manipulation
#adding
new_list = basket.extend([100, 101])
# print(new_list) #=>none
print(basket)

#removing
# removes last item you can add index -give the method and index
basket.pop()
new_list = basket.pop(3)
print(new_list)

# remove - here we give it the value we want removed
basket.remove(3)
print(basket)

# count
print(basket.count(11))

# sort modifies the list and sorted=> returns new list 
# reverse [::-1]

# generating a list 
print(list(range(1,101)))

# list into a string 
sentence = ' '.join(['hi', 'my', 'name', 'is', 'Moses'])
print(sentence)

# list unpacking
a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

#checking for duplicates in a list
some_list = ['a', 'b', 'c', 'd', 'd', 'b', 'f', 'g', 'a', 'i']

duplicates = [] # initialize empty list to store duplicates
for value in some_list:
  if some_list.count(value) > 1: #if value appears multiple times
    if value not in duplicates: # if value occurs multiple times is not in the list add
                                #it if there dont add, this prevents adding duplicates more than once
      duplicates.append(value)# add the value to the duplicate list
print(duplicates)

some_list2 = ['a', 'b', 'c', 'd', 'd', 'b', 'f', 'g', 'a', 'i']
duplicates = set([value for value in some_list2 if some_list2.count(value) > 1])
print(duplicates)

'''
list comprehensions
    it is a short hand form used instead of using normal for loop and append methods

    syntax: my_list[param(mutable) for param in iterable]
'''
#instead of
 
my_list = []
for char in 'hello':
  my_list.append(char)

print(my_list)

#do list comprehension
my_list = [char for char in 'hello there']
my_list1 = [num for num in range(0,100)]
my_list2 = [num**2 for num in range(0,30)]
my_list3 = [num**2 for num in range(0,50)if num % 2 ==0]


print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)


