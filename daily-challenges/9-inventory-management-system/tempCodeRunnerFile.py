import csv

class item_properties:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class management_system:
    def __init__(self):
        self.items = []
        

    def add_item(self, name, quantity, price):
        item = item_properties(name, quantity, price)
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                break

    def update_item(self, name, quantity, price):
        for item in self.items:
            if item.name == name:
                if quantity == 0 or quantity > 0:
                    item.quantity = quantity
                if price == 0 or price > 0:
                    item.price = price
                    break

    #display all inventory
    def display_inventory(self):
        for item in self.items:
            print(item)

    def load_inventory(self, filename):
        with open(filename, 'r') as inventoryfile:
            reader =csv.DictReader(inventoryfile)
            #loop through each row and print items
            for row in reader:
                item = item_properties(row['name'], int(row['quantity']), float(row['price']))
                self.items.append(item)

def main():
    



