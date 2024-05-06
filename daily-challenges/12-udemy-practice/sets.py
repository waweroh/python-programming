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



