# Sets -->unordered collections of unique objects
my_set = {1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 9}
my_set.add(100)
my_set.add(2)

print(my_set)  # sets only return unique values or objects no duplicates
print(len(my_set))
print(list(my_set)) #convert to list


# removing duplicates from a list
my_list = [1,2,3,3,4,4,5,6,7,8,9,9]
print(set(my_list))

# other important methods
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 9, 9, 10}

print(my_set.difference(your_set))
print(my_set) #didn't modify {1, 2, 3, 4, 5}
print(my_set.discard(5))
print(my_set)
print(my_set.difference_update(your_set))
print(my_set)# modified {1, 2, 4}
print(my_set.isdisjoint(your_set))#if they have nothing in common then True


# pairs same
print(my_set.intersection (your_set))
print(my_set & your_set)


print(my_set.union(your_set))
print(my_set | your_set)

# methods subset and superset


'''
list comprehensions
    it is a short hand form used instead of using normal for loop and append methods

    syntax: my_list[param(mutable) for param in iterable]
'''
#instead of
 
my_set = set()
for char in 'hello':
  my_set.add(char)

print(my_set)

#do list comprehension
my_set = {char for char in 'hello there'}
my_set1 = {num for num in range(0,100)}
my_set2 = {num**2 for num in range(0,30)}
my_set3 = {num**2 for num in range(0,50)if num % 2 ==0}


print(my_list)
print(my_set1)
print(my_set2)
print(my_set3)


