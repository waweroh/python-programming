def parse_file(file_path):

    with open (file_path, 'r') as f:
        file_contents = f.read()
    lines = file_contents.split('\n')  

    name_address_list = [] #init the list
    for line in lines:
        name_address_list.append (line.split(', '))
        # splitlines() method is called on the string to
        # split it into a list of strings, where each string represents a line from the file
        # for each line, the split(', ') method is called to 
        # split the line into a list using a comma and space as the delimiter.
        #  The resulting list is then appended to the name_address_list.
    
    address_book = {}
    for name_address in name_address_list:
        name_key = name_address[0] # key
        address_value = name_address [1] + ", " + name_address[2] #value
        address_book[name_key]= address_value
    return address_book
file_path = "addressbook.txt"
address_book = parse_file(file_path)
print (address_book)



