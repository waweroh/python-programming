import pandas

df = pandas.read_csv('hotels.csv', dtype={'id': str})
df_cards = pandas.read_csv('cards.csv', dtype=str).to_dict(orient='records')

class Hotel:
  def __init__(self, hotel_id):
    self.hotel_id = hotel_id
    self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()
    
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
    self.customer_name = customer_name
    self.hotel = hotel_object

  def generate(self):
    content = f'''
    Thank you for your reservation
    Here are your booking details
    Name: {self.customer_name}
    Hotel name: {self.hotel.name}
    '''
    return content
  
class CreditCard:
  def __init__(self, number):
    self.number = number

  def validate(self, expiration, holder, cvc):
    card_data = {'number':self.number, 'expiration':expiration, 
                 'holder':holder, 'cvc':cvc}
    if card_data in df_cards:
      return True
    else:
      return False

#program main loop or instances of the classes
print(df)
hotel_ID = input ('Enter the id of the Hotel: ')
hotel = Hotel(hotel_ID)

if hotel.available():
  credit_card = CreditCard(number='1234567890123456')
  if credit_card.validate(expiration='12/26', holder='Moses Waweru', cvc='123'):
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel) #instance of the ticket object
    print(reservation_ticket.generate()) #the instance points to the generate method to get the ticket
  else:
    print ('problem with payment')
else:
  print('Hotel not available')

