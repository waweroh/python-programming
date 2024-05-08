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