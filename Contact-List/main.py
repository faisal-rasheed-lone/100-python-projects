class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} - Phone: {self.phone_number}, Email: {self.email}"

class ContactGroup:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

    def __str__(self):
        return f"Group: {self.name}, Contacts: {len(self.contacts)}"

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.groups = {}

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            for group in self.groups.values():
                group.remove_contact(contact)

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = ContactGroup(group_name)

    def add_contact_to_group(self, contact, group_name):
        if group_name in self.groups:
            self.groups[group_name].add_contact(contact)

    def remove_contact_from_group(self, contact, group_name):
        if group_name in self.groups:
            self.groups[group_name].remove_contact(contact)

    def display_contacts(self):
        print("\nContacts:")
        for contact in self.contacts:
            print(contact)

    def display_groups(self):
        print("\nGroups:")
        for group in self.groups.values():
            print(group)

# Main Application
if __name__ == "__main__":
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Create Group")
        print("4. Add Contact to Group")
        print("5. Remove Contact from Group")
        print("6. Display Contacts")
        print("7. Display Groups")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == "2":
            contact_book.display_contacts()
            name = input("Enter the name of the contact to remove: ")
            for contact in contact_book.contacts:
                if contact.name == name:
                    contact_book.remove_contact(contact)
                    print(f"Contact '{name}' removed.")
                    break
            else:
                print(f"Contact '{name}' not found.")
        elif choice == "3":
            group_name = input("Enter group name: ")
            contact_book.create_group(group_name)
            print(f"Group '{group_name}' created.")
        elif choice == "4":
            contact_book.display_contacts()
            name = input("Enter the name of the contact to add to a group: ")
            group_name = input("Enter group name: ")
            for contact in contact_book.contacts:
                if contact.name == name:
                    contact_book.add_contact_to_group(contact, group_name)
                    print(f"Contact '{name}' added to group '{group_name}'.")
                    break
            else:
                print(f"Contact '{name}' not found.")
        elif choice == "5":
            contact_book.display_contacts()
            name = input("Enter the name of the contact to remove from a group: ")
            group_name = input("Enter group name: ")
            for contact in contact_book.contacts:
                if contact.name == name:
                    contact_book.remove_contact_from_group(contact, group_name)
                    print(f"Contact '{name}' removed from group '{group_name}'.")
                    break
            else:
                print(f"Contact '{name}' not found.")
        elif choice == "6":
            contact_book.display_contacts()
        elif choice == "7":
            contact_book.display_groups()
        elif choice == "8":
            print("Exiting the Contact Book Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
