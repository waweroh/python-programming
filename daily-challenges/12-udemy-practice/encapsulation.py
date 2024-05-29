'''
Encapsulation - is the binding of data/attributes and functions/methods
              that manipulate that data, encapsulating them in an objects
              ie. Class
It is similar to how other DS have access to various methods ie string has 
access to capitalize() method which is a function
'''
class PlayerCharacter:
  def __init__(self, name, power):
    self.name = name
    self.power = power 

  def run(self):
    print('run fast')

  def shout (self):
    print(f'My alias is {self.name} and power is {self.power}')

player1 = PlayerCharacter('superman', 89) 
print(player1.shout())
print(player1.run())
