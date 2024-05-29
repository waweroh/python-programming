class BigObject:
  pass
print(type(BigObject)) #<class 'type'>
obj1 = BigObject()
print(type(obj1)) #<class '__main__.BigObject'>(instantiation)

# class can be instantiated into other instances(objects)

#another class
'''
  constructor method --is called whenever we instantiate.
  When we call init during instantiation we accept what is after
  self as the parameter.
  self --- When you create an object (also known as an instance) from 
          a class, self refers to that specific instance every time the class is instantiated.

'''
class PlayerCharacter:
  #class object attribute -- it's not dynamic across instances 
  membership = True

  def __init__(self, name, age ): 
    if (self.membership):
      self.name = name #attributes - dynamic pieces of data across instances
      self.age = age
  
  def shout (self):
    print(f'my name is {self.name}, age is {self.age}')

  #class method 
  '''
  creates method for the class this methods can be used without instantiating 
  the class but you can still instantiate it at the return level if need be.
  They are not used often
  '''
  @classmethod
  def adding_things(cls, num1, num2):
     return num1 + num2
  

  #static method
  '''
  here we do not have access to the class.We use it when we have no use for class attributes

  '''
  @staticmethod
  def adding_things2( num1, num2):
    return num1 + num2


    

player1 = PlayerCharacter('moses', 144)
player2 = PlayerCharacter('stephen', 56)
player2.attack = 50 # You can now assign methods to the instances


print(player1.name)
print(player1.membership)
print(player2.age)
print(player1.shout())
print(player2.attack)
print(player2.adding_things2(30,50)) #using staticmethod
print(player1.adding_things(49,6)) #classmethod
print(PlayerCharacter.adding_things(34,6)) #classmethod without instantiation

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('dan', 10)
cat2 = Cat('amy', 13)
cat3 = Cat('nina', 4)





# 2 Create a function that finds the oldest cat
'''
1.  Sorting with Lambda: small anonymous function without def keyword

    You can use a lambda function as the key for sorting a
    list of tuples by the second element:
*args- prints positional arguments into a tuple in this case a list of tuples since
       we have 3 cat objects 
'''
def oldest_cat(*args):
    oldest = max(args, key=lambda cat: cat.age)
    return oldest
   


thatOld_cat = oldest_cat(cat1, cat2, cat3)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'Oldest cat is {thatOld_cat.name} who is {thatOld_cat.age} years old.')


  
  
