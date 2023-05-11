class bank:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount