# tuple --> is immutable
my_tuples =(1, 2, 3, 4,4, 5,5,5, 6)
x = my_tuples[0]
y = my_tuples[1]
z = my_tuples[2: 4]

# Methods
print(my_tuples.index(5))
print(my_tuples.count(5)) #count how many fives
print(len(my_tuples))



# alternative 
x,y,z,*other = my_tuples
print (z)
print (x)
print (other)