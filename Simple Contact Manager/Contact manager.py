# Define the contact list as a dictionary
contacts = {}

def add_contact(name, phone, email):
    """Add a new contact to the contacts dictionary."""
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact {name} added.")

def view_contacts():
    """Display all contacts."""
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {details['Phone']}")
            print(f"  Email: {details['Email']}")
    else:
        print("No contacts to display.")

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"  Phone: {details['Phone']}")
        print(f"  Email: {details['Email']}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

# Main program loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
