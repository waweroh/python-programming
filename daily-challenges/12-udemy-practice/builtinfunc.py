# greet = 'Helloooo'
# print(greet[0:len(greet)])

# quote = 'to be or not to be'
# print(quote.capitalize())

# birth_year = input('birth_year')
# age = 2024 - int(birth_year)
# print (f'age is : {age}')

name = input('name: ')
password = input('password: ')
pass_len = len(password)
password_hide = '*' * pass_len


print (f'{name} your password {password_hide} is {pass_len} letters long')