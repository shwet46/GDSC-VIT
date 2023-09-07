def display_contact(contact):
    print("Name:", contact['name'])
    print("Email:", contact['email'])
    print("Phone:", contact['phone'])

def add_contact(contacts):
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    contact = {'name': name, 'email': email, 'phone': phone}
    contacts[name] = contact
    print("Contact added successfully.")

def update_contact(contacts):
    name = input("Enter name to update: ")
    if name in contacts:
        print("Current contact information:")
        display_contact(contacts[name])

        email = input("Enter new email (press Enter to keep current): ")
        phone = input("Enter new phone (press Enter to keep current): ")

        if email:
            contacts[name]['email'] = email
        if phone:
            contacts[name]['phone'] = phone

        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = {}

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            update_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("\nAll Contacts:")
            for name, contact in contacts.items():
                print("\nContact:", name)
                display_contact(contact)
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
