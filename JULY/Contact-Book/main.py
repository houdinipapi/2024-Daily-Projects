import json
import os


# File to store the contacts
contacts_file = "contacts.json"

def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            return json.load(file)
        
    return []


def save_contacts(contacts):
    with open(contacts_file, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")


def view_contacts(contacts):
    if contacts:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")
    else:
        print("No contacts found!")


def search_contact(contacts):
    search_name = input("Enter the name to search: ")
    found_contacts = [
        contact for contact in contacts if search_name.lower() in contact['name'].lower()
    ]

    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")
    else:
        print("No contacts found with that name!")

def delete_contact(contacts):
    delete_name = input("Enter the name to delete: ")
    new_contacts = [
        contact for contact in contacts if delete_name.lower() != contact['name'].lower()
    ]
    if len(new_contacts) == len(contacts):
        print("No contacts found with that name!")
    else:
        save_contacts(new_contacts)
        print(f"Contact {delete_name} deleted successfully!")
    
    return new_contacts

def edit_contact(contacts):
    edit_name = input("Enter the name to edit: ")
    for contact in contacts:
        if edit_name.lower() in contact["name"].lower():
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")
            contact["name"] = input("Enter new name (leave blank to keep current): ") or contact["name"]
            contact["phone_number"] = input("Enter new phone number (leave blank to keep current): ") or contact["phone_number"]
            contact["email"] = input("Enter new email (leave blank to keep current): ") or contact["email"]
            print("Contact updated successfully!")
            save_contacts(contacts)  # Save changes after editing the contact
            return contacts
    print("No contacts found with that name!")
    return contacts


def sort_contacts(contacts):
    print("Sort contacts by: 1. Name 2. Phone 3. Email")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        contacts.sort(key=lambda x: x["name"].lower())
    elif choice == "2":
        contacts.sort(key=lambda x: x["phone_number"])
    elif choice == "3":
        contacts.sort(key=lambda x: x["email"].lower())
    else:
        print("Invalid choice! Sorting by name as default.")
        contacts.sort(key=lambda x: x["name"].lower())
    print("Contacts sorted successfully!")
    return contacts


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Sort Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            contacts = delete_contact(contacts)
        elif choice == "5":
            contacts = edit_contact(contacts)
        elif choice == "6":
            contacts = sort_contacts(contacts)
        elif choice == "7":
            save_contacts(contacts)
            print("Exiting the program...\nGoodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()