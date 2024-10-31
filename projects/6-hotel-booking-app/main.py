import pandas

df = pandas.read_csv('hotels.csv')

class Hotel:
  def __init__(self, id):
    pass
    
  def book(self):
    pass

  def available(self):
    pass


class ReservationTicket:
  def __init__(self, customer_name, hotel_object):
    pass

  def generate(self):
    pass

#program main loop or instances of the classes
print(df)
id = input ('Enter the id of the Hotel: ')
hotel = Hotel(id)

if hotel.available():
  hotel.book()
  name = input('Enter your name: ')
  reservation_ticket = ReservationTicket(name, hotel) #instance of the ticket object
  reservation_ticket.generate() #the instance points to the generate method to get the ticket

