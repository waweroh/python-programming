'''
Polymorphism - many forms.refer to how object classes can share the 
               same method name, but those method names can act differently
               based on what objects calls them.
In this case attack method is redefined in both the Grandmaster and Shaolin_archer
class and acts in the different ways it is set under those classes.

super() - used to call a cooperative superclass method ie the attributes within init
'''
class User: #PARENT CLASS
  def __init__(self,email):
    self.email = email

  def sign_in(self):
    print('logged in')

class Grandmaster(User):# user class inherited in Grandmaster class
  def __init__(self, name, power,email):
    super().__init__(email)
    self.name = name
    self.power = power

  def attack(self): #polymorphism
    print(f'attacking with a power of {self.power} ')

class Shaolin_archer(User):# user class inherited in archer class
  def __init__(self, name, num_arrows,email):
    super().__init__(email)
    self.name = name
    self.num_arrows = num_arrows

  def attack(self): #polymorphism
    print(f'attacking with {self.num_arrows} arrows left')
grandmaster1 = Grandmaster('Master Wong', 88, 'moses@gmail.com')
archer1 = Shaolin_archer('Lu', 24, 'lu@gmail.com')
grandmaster1.attack() #polymorphism
archer1.attack() #polymorphism
print (grandmaster1.email)
print (archer1.email)

#introspection
print(dir(grandmaster1))
print(help(max))

