contact = {}

def display_contact(contact):
    for name, phone_num in contact.items:
        print(f"Name: {name}, Phone number: {phone_num}")



while True:
    option = int(input("1. Add new contact \n2. Delete contact \n3. Search contact \n4. Display all contacts \n Enter your choice "))

    if option == 1:
        name = input("enter the contact name: ")
        phone_num = int(input("Enter the phone number:"))
        contact[name] = phone_num

    elif option == 2:
        del_contact = input("Enter contact to be deleted:")
        if del_contact == contact:
            contact.pop(del_contact)

    elif option == 3:
        search_name = input("Enter the search name: ")
        if search_name in contact:
            print(search_name,"'s contact number is ", contact[name])
        else:
            print("Name is not in contact list")
    
    elif option == 4:
        if not contact:
            print("empty contact list")
        else:
            display_contact()

    
    
        