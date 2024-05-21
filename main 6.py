import colorama
import random

class Contact:
    def __init__(self, name, phone_number, email, type):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.type = type

# Contacts are objects initialised with 3 attributes.
# We have incorporated an additional type attribute so identify the kind of contact.

class Work(Contact):
    def __init__(self, name, phone_number, email, type, work_email, company_name):
        self.work_email = work_email
        self.company_name = company_name
        super().__init__(name, phone_number, email, type)

class Friend(Contact):
    def __init__(self, name, phone_number, email, type, birthday):
        self.birthday = birthday
        super().__init__(name, phone_number, email, type)

class Emergency(Contact):
    def __init__(self, name, phone_number, email, type, secondary_phone_number):
        self.secondary_phone_number = secondary_phone_number
        super().__init__(name, phone_number, email, type)
    
# These are sub classes of class Contact, they have additional attributes, in addition to the attributes they inherited from the parent class

class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com", "standard"),
            Contact("Bob", "9876543210", "bob@email.com", "standard")
        ]

# ContactBook objects created from this class are initialised with a list attribute containing 2 Contact objects.

    def sort_contacts(self):
        self.contacts = sorted(self.contacts, key=lambda contact: contact.name)

# The sorted function sorts the list (argument 1) using the key in argument 2. A lambda function is used to sort by contact name
# because the sorted function requires argument 2 to be a function for some reason, so I couldn't simply put argument 2 as
# 'contact.name'. We got the idea to use a lambda function as the argument for the sorted function from chatgpt, it is the only
# time a large language model (LLM) was used on this project.

    def add_contact(self, name, phone_number, email, type):
            for contact in self.contacts:
                if contact.name == name:
                    print("There is already a contact with this name.") # Returns to main code block without making changes if the contact
                    return                                              # already exists. No duplicates.
            if type == "standard":
                    new_contact = Contact(name, phone_number, email, type) # Creates contact object to be added to contacts list.
                    self.contacts.append(new_contact)
                    print(f"Contact '{name}' added successfully.")
                    
            elif type == "work":
                    work_email = input("Enter work email: ")
                    company_name = input("Enter company name: ")
                    new_contact = Work(name, phone_number, email, type, work_email, company_name) # Creates contact object to be added to contacts list.
                    self.contacts.append(new_contact)
                    print(f"Contact '{name}' added successfully.")
                    
            elif type == "friend":
                    birthday = input("Enter birthday: ")
                    new_contact = Friend(name, phone_number, email, type, birthday) # Creates contact object to be added to contacts list.
                    self.contacts.append(new_contact)
                    print(f"Contact '{name}' added successfully.")
                    
            elif type == "emergency":
                    emergency = input("Enter secondary phone number: ")
                    new_contact = Emergency(name, phone_number, email, type, emergency) # Creates contact object to be added to contacts list.
                    self.contacts.append(new_contact)
                    print(f"Contact '{name}' added successfully.")
                    

    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for contact in self.contacts: # Using a for loop to cycle through the list of objects is a recurring theme.
                if contact.type == "standard": # If statement used to print details relevant to the type of contact.
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                elif contact.type == "work":
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\nWork Email: {contact.work_email}\nCompany Name: {contact.company_name}\n")
                elif contact.type == "friend":
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\nBirthday: {contact.birthday}\n")
                elif contact.type == "emergency":
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\nSecondary Phone Number: {contact.secondary_phone_number}\n")
        else:
            print("No contacts found.")

# This methods prints every object in the list by using a for loop to cycle through the list one item at a time.

    def search(self):
        print("Which contact would you like to find? Please type name.")
        contact_to_find = input(" > ").capitalize()
        for contact in self.contacts:
            if contact.name == contact_to_find:
                if contact.type == "standard":
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                elif contact.type == "work":
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\nWork Email: {contact.work_email}\nCompany Name: {contact.company_name}\n")
                elif contact.type == "friend":
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\nBirthday: {contact.birthday}\n")
                elif contact.type == "emergency":
                    print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\nSecondary Phone Number: {contact.secondary_phone_number}\n")

# Search method works similar to display all method, but only prints contacts in which name property matches the search. Given that there
# are no duplicates allowed this should only ever print 1 result if any.
                  
    def update(self):
        print("Which contact would you like to update? Please type name.")
        contact_to_find = input(" > ").capitalize()
        contact_in_list = False # Using a boolean variable to track this is probably sloppy coding but at least it works.
        for contact in self.contacts:
            if contact.name == contact_to_find:
                contact_in_list = True
                contact_type = contact.type
        if contact_in_list == False:
            print("I am sorry there is no contact with that name.")
        else:
            if contact_type == "standard": # We used functions here purely so we can collapse them in VSC so its easier to read.
                def standard_grrr():
                    while True: # While loop used so will keep asking user for input until they enter valid input.
                        print("Would you like to update the phone number or email? Please type \'email\', \'phone\' or \'both\'.")
                        # Used escape characters because was concerned it would break something.
                        update_option = input(" > ").lower() # Gives option to update contact details based on input.
                        if update_option == "email" or update_option == "both":
                            for contact in self.contacts:
                                if contact.name == contact_to_find:
                                    print("Please enter the new email.")
                                    new_email = input(" > ")
                                    contact.email = new_email
                                    print("Email has been updated.")
                            
                        if update_option == "phone" or update_option == "both":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new phone number.")
                                        new_number = input(" > ")
                                        contact.phone_number = new_number
                                        print("Phone number has been updated.")
                                
                        if update_option != "both" and update_option != "email" and update_option != "phone":
                            print("please type in one of the options provided")
                        else:
                            break
                standard_grrr()           
            elif contact_type == "work":
                def work_grrr():
                    while True: # While loop used so will keep asking user for input until they enter valid input.
                        print("What would you like to update? Please type \'email\', \'phone\', \'work email\', \'company name\' or \'all\'.")
                        # Used escape characters because was concerned it would break something.
                        update_option = input(" > ").lower() # Gives option to update contact details based on input.
                        if update_option == "email" or update_option == "all":
                            for contact in self.contacts:
                                if contact.name == contact_to_find:
                                    print("Please enter the new email.")
                                    new_email = input(" > ")
                                    contact.email = new_email
                                    print("Email has been updated.")
                            
                        if update_option == "phone" or update_option == "all":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new phone number.")
                                        new_number = input(" > ")
                                        contact.phone_number = new_number
                                        print("Phone number has been updated.")
                                
                        if update_option == "work email" or update_option == "all":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new work email.")
                                        work_email = input(" > ")
                                        contact.work_email = work_email
                                        print("Work email has been updated.")
                                
                        if update_option == "company name" or update_option == "all":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new company name.")
                                        company_name = input(" > ")
                                        contact.company_name = company_name
                                        print("Company name has been updated.")
                                
                        if update_option != "company name" and update_option != "all" and update_option != "email" and update_option != "phone" and update_option != "work email":
                            print("please type in one of the options provided")
                        else:
                            break
                work_grrr()
            elif contact_type == "friend":
                def friend_grrr():
                    while True: # While loop used so will keep asking user for input until they enter valid input.
                        print("What would you like to update? Please type \'email\', \'phone\', \'birthday\', or \'all\'.")
                        # Used escape characters because was concerned it would break something.
                        update_option = input(" > ").lower() # Gives option to update contact details based on input.
                        if update_option == "email" or update_option == "all":
                            for contact in self.contacts:
                                if contact.name == contact_to_find:
                                    print("Please enter the new email.")
                                    new_email = input(" > ")
                                    contact.email = new_email
                                    print("Email has been updated.")
                            
                        if update_option == "phone" or update_option == "all":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new phone number.")
                                        new_number = input(" > ")
                                        contact.phone_number = new_number
                                        print("Phone number has been updated.")
                                
                        if update_option == "birthday" or update_option == "all":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new birthday.")
                                        new_number = input(" > ")
                                        contact.birthday = new_number
                                        print("The birthday has been updated.")
                                
                        if update_option != "birthday" and update_option != "all" and update_option != "email" and update_option != "phone":
                            print("please type in one of the options provided")
                        else:
                            break
                friend_grrr()
            elif contact_type == "emergency":
                def emergency_grrr():
                    while True: # While loop used so will keep asking user for input until they enter valid input.
                        print("What would you like to update? Please type \'email\', \'phone\', \'secondary phone number\', or \'all\'.")
                        # Used escape characters because was concerned it would break something.
                        update_option = input(" > ").lower() # Gives option to update contact details based on input.
                        if update_option == "email" or update_option == "all":
                            for contact in self.contacts:
                                if contact.name == contact_to_find:
                                    print("Please enter the new email.")
                                    new_email = input(" > ")
                                    contact.email = new_email
                                    print("Email has been updated.")
                            
                        if update_option == "phone" or update_option == "all":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new phone number.")
                                        new_number = input(" > ")
                                        contact.phone_number = new_number
                                        print("Phone number has been updated.")
                                
                        if update_option == "secondary phone number" or update_option == "all":
                                for contact in self.contacts:
                                    if contact.name == contact_to_find:
                                        print("Please enter the new secondary phone number.")
                                        new_number = input(" > ")
                                        contact.secondary_phone_number = new_number
                                        print("The secondary phone number has been updated.")
                                
                        if update_option != "secondary phone number" and update_option != "all" and update_option != "email" and update_option != "phone":
                            print("please type in one of the options provided")
                        else:
                            break
                emergency_grrr()
    
    
    def delete(self):
        print("Which contact would you like to delete? Please type name.")
        contact_to_delete = input(" > ").capitalize()
        for contact in self.contacts: 
            if contact.name == contact_to_delete:
                self.contacts.remove(contact)
                print("", contact_to_delete, "has been deleted.")     

def main():
    contact_book = ContactBook() # Contact book object is initialised from the class.

    while True: # The structure of the main block of code for this program was laid out by Katy. Simple enough repeats menu options.
        num = random.randint(1, 9) # Changes colour every cycle because stretch goal.
        if num == 1:
            print(colorama.Fore.RED, colorama.Back.LIGHTRED_EX)
        elif num == 2:
            print(colorama.Fore.GREEN, colorama.Back.LIGHTGREEN_EX)
        elif num == 3:
            print(colorama.Fore.BLUE, colorama.Back.LIGHTYELLOW_EX)
        elif num == 4:
            print(colorama.Fore.RED, colorama.Back.LIGHTCYAN_EX)
        elif num == 5:
            print(colorama.Fore.CYAN, colorama.Back.LIGHTMAGENTA_EX)
        elif num == 6:
            print(colorama.Fore.RED, colorama.Back.LIGHTBLACK_EX)
        elif num == 7:
            print(colorama.Fore.RED, colorama.Back.LIGHTBLUE_EX)
        elif num == 8:
            print(colorama.Fore.RED, colorama.Back.LIGHTWHITE_EX)
        elif num == 9:
            print(colorama.Fore.RED, colorama.Back.LIGHTGREEN_EX)

        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search For Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Sort Contacts Alphabetically")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            type = input("Is this a standard, work, friend or emergency contact?").lower()
            name = input("Enter name: ").capitalize()
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ").lower()
            contact_book.add_contact(name, phone_number, email, type)
        elif choice == "2":
            contact_book.display_all_contacts()
        elif choice == "3":
            contact_book.search()
        elif choice == "4":
            contact_book.update()
        elif choice == "5":
            contact_book.delete()
        elif choice == "6":
            contact_book.sort_contacts()
            print("Your contacts have been sorted in alphabetical order.")
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            print(colorama.Fore.RESET, colorama.Back.RESET)
            break
        else:
            print("invalid input")

if __name__ == "__main__":
    main()