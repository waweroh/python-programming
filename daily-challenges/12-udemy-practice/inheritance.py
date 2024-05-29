'''
Inheritance - allows a class to inherit attributes and methods from another class. 
              This helps in promoting code reuse and establishing a hierarchical 
              relationship between classes.

'''

class User: #PARENT CLASS
  def sign_in(self):
    print('logged in')

class Grandmaster(User):# user class inherited in Grandmaster class
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with a power of {self.power} ')

class Shaolin_archer(User):# user class inherited in archer class
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with {self.num_arrows} arrows left')

grandmaster1 = Grandmaster('Master Wong', 88)
archer1 = Shaolin_archer('Lu', 24)
print(grandmaster1.sign_in()) #inheritance of user in grandmaster class
archer1.sign_in() #inheritance of user in archer class
grandmaster1.attack()
archer1.attack()