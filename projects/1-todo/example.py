# for i,j in enumerate('name'):
#   print(i + 1)

# menu = ["pasta", "pizza", "salad"] 
# user_choice = int(input("Enter the index of the item: "))
# message = f"You chose {menu[user_choice]}"
# print(message)
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# texts = ['hello','hello','hello']
# for text, filename in zip(texts, filenames):
#   file = open(f'files/{filename}', 'w')
#   file.write(text)
def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum
    
celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32
 
print(fahrenheit)