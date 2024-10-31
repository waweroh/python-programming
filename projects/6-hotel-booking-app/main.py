import pandas

df = pandas.read_csv('hotels.csv', dtype={'id': str})

class Hotel:
  def __init__(self, hotel_id):
    self.hotel_id = hotel_id
    
  def book(self):
    '''Book a hotel by changing its availability to NO'''
    df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
    df.to_csv('hotels.csv', index=False)

  def available(self):
    '''Checks whether hotel is available'''
    availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
    if availability == 'yes':
      return True
    else:
      return False



class ReservationTicket:
  def __init__(self, customer_name, hotel_object):
    pass

  def generate(self):
    pass

#program main loop or instances of the classes
print(df)
hotel_ID = input ('Enter the id of the Hotel: ')
hotel = Hotel(hotel_ID)

if hotel.available():
  hotel.book()
  name = input('Enter your name: ')
  reservation_ticket = ReservationTicket(name, hotel) #instance of the ticket object
  reservation_ticket.generate() #the instance points to the generate method to get the ticket
else:
  print('Hotel not available')

