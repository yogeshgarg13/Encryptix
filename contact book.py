class Contact:
  def __init__(self, name, phone, email, address):
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address

class ContactBook:
  def __init__(self):
    self.contacts = []

  def add_contact(self, contact):
    self.contacts.append(contact)

  def view_contacts(self):
    print("Contact List")
    print("-------------")
    for contact in self.contacts:
      print(f"Name: {contact.name}")
      print(f"Phone: {contact.phone}")
      print(f"Email: {contact.email}")
      print(f"Address: {contact.address}")
      print()

  def search_contacts(self, keyword):
    results = []
    for contact in self.contacts:
      if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone:
        results.append(contact)
    return results

  def update_contact(self, contact_index, new_contact):
    if 0 <= contact_index < len(self.contacts):
      self.contacts[contact_index] = new_contact

  def delete_contact(self, contact_index):
    if 0 <= contact_index < len(self.contacts):
      del self.contacts[contact_index]

def main():
  contact_book = ContactBook()

  while True:
    print("Contact Book")
    print("------------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice (1/2/3/4/5/6): "))

    if choice == 1:
      name = input("Enter the name: ")
      phone = input("Enter the phone number: ")
      email = input("Enter the email: ")
      address = input("Enter the address: ")
      contact = Contact(name, phone, email, address)
      contact_book.add_contact(contact)

    elif choice == 2:
      contact_book.view_contacts()

    elif choice == 3:
      keyword = input("Enter the name or phone number to search: ")
      results = contact_book.search_contacts(keyword)
      for i, result in enumerate(results):
        print(f"{i+1}. {result.name} ({result.phone})")

    elif choice == 4:
      index = int(input("Enter the index of the contact to update: ")) - 1
      if 0 <= index < len(contact_book.contacts):
        name = input("Enter the new name: ")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        address = input("Enter the new address: ")
        new_contact = Contact(name, phone, email, address)
        contact_book.update_contact(index, new_contact)

    elif choice == 5:
      index = int(input("Enter the index of the contact to delete: ")) - 1
      if 0 <= index < len(contact_book.contacts):
        contact_book.delete_contact(index)

    elif choice == 6:
      break

    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()
