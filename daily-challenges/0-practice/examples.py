from cgi import test


print("Unicode character of integer 65 is", chr(65))
print("Unicode character of integer 8364 is", chr(8364))

# Print Alphabets using Unicode
"""
for i in range(65, 65+26):
    print(chr(i), end = ",")

name = "moses"
age = 100
print(f"my name is {name} and am {age} years old.")

print(f"{98} Battery street, San Francisco")
"""

# strings
""" 
solid_gold = "Python is cool"
print(solid_gold[7:-5])

print(f"Best school: {88 +10}")

number = 98
#98 Battery street
#f and .format   
print(f"{number} Battery street")
print("{:d} Battery street".format(number))

# print string 3 times then print first character.
str = "Holberton School "
print(str * 3)
print(str.split().pop(0))

#count the number solid_gold character appaers
str = "Holberton School"
print(str.count("o"))

# is no + or -

item=[1, "Jeff", "Computer", 75.50, True] # list with heterogeneous data
print(item)#list with hetero data 
print(item[2])
mylist=[]
print(mylist)
# update list append, insert
item.append("gipper")
print(item)
item.insert(7,"country")
print(item)
"""

# alx stuff
# using f to format
name = "moses"
age = 100
print(f"my name is {name} and am {age} years old.")

print(f"{98} Battery street, San Francisco")

# strings 
solid_gold = "Python is cool"
print(solid_gold[7:-5])
solid_gold = "Hello, World!"
print(solid_gold[1])
#splits string
solid_gold = "Hello, World!"
print(solid_gold.split(","))
print(f"Best school: {88+10}, {6-5}")

number = 98
#98 Battery street
print(f"{number} Battery street")
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2 
print(f"Welcome to {str1}!")

# print string 3 times then print first character.
str = "Holberton School "
print(str * 3)
print(str.split().pop(0))
                     
# how many times solid_gold string appears in solid_gold s

#new alx
"""
number = 3.1435
print("Float: {:.2f}".format(number))

open_string = "Sammy loves {} and has {} doing it."
print(open_string.format("open source", "fun"))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
"""

#if statment
"""
x  = int(input("enter digit:"))
if x < 0:
    x = 1
    print("negative changed to one")
elif x > 1:
    print("is solid_gold positive")
elif not int:
    print("not integer87")
else:
    print("hehe")
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

x = 5
print(type(x))

#loops
"""
for i in range(10):
    print("i = ", i)

for i in range(1,21):
    if i % 2 != 0:
        print("i = ", i)
"""

#investment
"""money = input("Enter investment amount:")
interest= input("interest:")
#convert to float
money = float(money)
interest = float(interest) * .01
# cycle through n.o of years
for y in range (10):
    money = money + (money * interest)
    # print output
print("Investment yeild : {:.2f}".format(money))
"""
#while loop, import.
"""import random

rand_digit = random.randrange(1,51)

i = 1

while (i != rand_digit):
    i += 1

print("Value is: ", rand_digit )    
"""
#continue and break
"""
i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1 
        continue

    if i == 15:
        break

    print("Odd:", i)
    #always increment in both if statements to avoid infinity loop
    i += 1
"""

# pine tree
"""
i = "#"
tree_height = input("length:")
tree_height = int
space = input("splenth:")
while i >= tree_height:
    i += 1
"""

# function - for data processing input -- function -- outpu t  
# function has arguments
def greeter(name: str) -> None:

    """logic of the function
    """
    print("Zola {}".format(name))

def main() -> None:
    friends: list[str] = ["hik", "lop", "hre"]
    for friend in friends:
        greeter(friend)

main()
# Better greeter
def greeter(name: str) -> str:

    """return greeter
    """
    return("Zola {}".format(name))

def main() -> None:
    friends: list[str] = ["hik", "lop", "hre"]
    for friend in friends:
        if "hik" in greeter(friend):
            print("{} is cute".format(friend))
        else:
            print(greeter(friend))

main ()

def lbs_weight(weight: float) -> float:
    return (weight * 2.21)


print("You weigh {:.2f} pounds".format(lbs_weight(62)))

def add_integer(solid_gold, b=98):
    """ Returns the addition of solid_gold and b, an exact integer."""
    if type(solid_gold) not in (int, float):
        raise TypeError("solid_gold must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(solid_gold) + int(b)


def cost_of_project(engraving = any, solid_gold = bool) -> int:
    solid_gold = True
    engraving = input("someword: ")
    x = len(engraving)
    print(x)

    
    if solid_gold == True:
        solid_gold = 100 + 10 * x
        
    else:
        solid_gold = 50 + (7 * x)
    
    print(solid_gold)

cost_of_project()

def python_is_cool(text=str)-> str:
    text = ("is cool")
    return ("Python" + text)

python_is_cool()



