contacts = []

def add_contact():
    store_name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        "Store Name": store_name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n=== Contact List ===")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['Store Name']} - {contact['Phone']}")
    print()

def search_contact():
    keyword = input("Search by Name or Phone: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact["Store Name"].lower() or keyword in contact["Phone"]:
            print("\n=== Contact Found ===")
            print(f"Store Name: {contact['Store Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}\n")
            found = True
    if not found:
        print("No matching contact found.\n")

def update_contact():
    view_contacts()
    index = int(input("Enter contact number to update: ")) - 1
    if 0 <= index < len(contacts):
        print("Leave blank to keep current value.")
        contact = contacts[index]
        store_name = input(f"New Store Name [{contact['Store Name']}]: ") or contact['Store Name']
        phone = input(f"New Phone [{contact['Phone']}]: ") or contact['Phone']
        email = input(f"New Email [{contact['Email']}]: ") or contact['Email']
        address = input(f"New Address [{contact['Address']}]: ") or contact['Address']
        contacts[index] = {
            "Store Name": store_name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact updated successfully!\n")
    else:
        print("Invalid contact number.\n")

def delete_contact():
    view_contacts()
    index = int(input("Enter contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        deleted = contacts.pop(index)
        print(f"Deleted contact: {deleted['Store Name']}\n")
    else:
        print("Invalid contact number.\n")

def menu():
    while True:
        print("==== Contact Management ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
