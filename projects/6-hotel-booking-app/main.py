import pandas

df = pandas.read_csv('hotels.csv')

class Hotel:
  def __init__(self, id):
    pass
    
  def book(self):
    pass


class ReservationTicket:
  def generate(self):
    pass

#program main loop or instances of the classes
print(df)
id = input ('Enter the id of the Hotel: ')
hotel = Hotel(id)
