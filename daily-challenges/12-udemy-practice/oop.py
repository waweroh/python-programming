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
    

player1 = PlayerCharacter('moses', 144)
player2 = PlayerCharacter('stephen', 56)
player2.attack = 50 # You can now assign methods to the instances

print(player1.name)
print(player1.membership)
print(player2.age)
print(player1.shout())
print(player2.attack)


  
  
