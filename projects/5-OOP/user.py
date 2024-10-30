class User:

  def __init__(self, name, birth_year):
    self.name = name
    self.birth_year = birth_year

  def get_name(self):
    return self.name.upper()

  def age(self, current_year):
    age = current_year - self.birth_year
    return age

user1 = User('John', 1999)
print(user1.age(2023))
print(user1.get_name())