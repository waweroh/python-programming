'''
Inheritance - allows a class to inherit attributes and methods from another class. 
              This helps in promoting code reuse and establishing a hierarchical 
              relationship between classes.

'''


class Grandmaster():# user class inherited in Grandmaster class
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with a power of {self.power} ')

class Shaolin_archer():# user class inherited in archer class
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with {self.num_arrows} arrows left')
    
# MULTIPLE INHERITANCE
class Grand_specialist(Grandmaster, Shaolin_archer):
  def __init__(self, name, power, num_arrows):
    Grandmaster.__init__(self, name, power)
    Shaolin_archer.__init__(self, name, num_arrows)

grand_spec1 = Grand_specialist('jorge',50,43)
print(grand_spec1.num_arrows)
print(grand_spec1.power)

