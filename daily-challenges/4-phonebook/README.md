# Phonebook

<p>The code initializes an empty dictionary called contact to store the contacts.
The display_contact(contact) function is defined to display the name and phone number of each contact stored in the contact dictionary.
The code enters an infinite loop using while True.
Inside the loop, it prompts the user to enter an option by displaying a menu of choices using the input() function. The selected option is stored in the option variable after converting it to an integer.
Based on the selected option, the code executes the corresponding block of code:</p>

- If option is 1, it prompts the user to enter a contact name and phone number. The name and phone number are then added to the contact dictionary.

- If option is 2, it prompts the user to enter a contact name to be deleted. If the contact name exists in the contact dictionary, it is removed using the pop() method. The display_contact() function is then called to display the updated contact list.

- If option is 3, it prompts the user to enter a contact name to search for. If the contact name exists in the contact dictionary, it prints the corresponding phone number. Otherwise, it displays a message indicating that the name is not in the contact list.

- If option is 4, it checks if the contact dictionary is empty. If it is, it prints a message indicating an empty contact list. Otherwise, it calls the display_contact() function to display all the contacts.

<p>The loop continues indefinitely until the user decides to exit or terminate the program.</p>