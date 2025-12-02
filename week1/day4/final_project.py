class ContactBook:
    def __init__(self):
        self.contacts_file = 'ContactBook.json'

    def create_contact(self, id, name, phone, email, address):
        contact = {
            "id": id,
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        # Load existing contacts
        try:
            with open(self.contacts_file, 'r') as f:
                contacts = json.load(f)
        except:
            contacts = []

        if isinstance(contacts, dict):
          contacts = [contacts]

        contacts.append(contact)

        with open(self.contacts_file, 'w') as f:
            json.dump(contacts, f, indent=4)

        print("Contact created successfully.")

      
    def delete_contact(self, id):
       try:
         with open(self.contacts_file, 'r') as f:
            contacts_data = json.load(f)

         new_contacts_data = []

         for c in contacts_data:
            # If this is a nested "contacts" list, handle separately
            if "contacts" in c:
                 new_list = []
                 for contact in c["contacts"]:
                   if contact["id"] != id:
                    new_list.append(contact) 
                 c["contacts"] = new_list
                 new_contacts_data.append(c)
            else:
                if c.get("id") != id:
                    new_contacts_data.append(c)

         if len(new_contacts_data) == len(contacts_data):
            print("No contact found with this ID.")
            return

         with open(self.contacts_file, 'w') as f:
            json.dump(new_contacts_data, f, indent=4)

         print(f"Contact(s) with ID {id} deleted successfully.")

       except FileNotFoundError:
         print("Contacts file not found.")
       except Exception as e:
         print("An error occurred:", e)



    def update_contact(self, id, name, phone, email, address):
       try:
        with open(self.contacts_file, 'r') as f:
            contacts_data = json.load(f)

        contact_found = False

        # Loop through contacts
        for c in contacts_data:
            if "contacts" in c:
                for contact in c["contacts"]:
                    if contact["id"] == int(id):
                        contact_found = True
                        contact["name"] = name
                        contact["phone"] = phone
                        contact["email"] = email
                        contact["address"] = address
            else:
                if c.get("id") == int(id):
                    contact_found = True
                    c["name"] = name
                    c["phone"] = phone
                    c["email"] = email
                    c["address"] = address

        if not contact_found:
            print("No contact found with this ID.")
            return

        # Save updated data
        with open(self.contacts_file, 'w') as f:
            json.dump(contacts_data, f, indent=4)

        print(f"Contact with ID {id} updated successfully.")

       except FileNotFoundError:
        print("Contacts file not found.")
       except Exception as e:
        print("An error occurred:", e)
    
        
    def read_contacts(self):
       with open(self.contacts_file, 'r') as f:
        view = f.readlines()
        finalreviw= list(view)   
        for e in finalreviw:
           print(e.strip())

if __name__ == "__main__":
   import json
   contactor=ContactBook()
while True:
    print("contact book final project")
    print("enter 1 to add contact")
    print("enter 2 to delete contact")
    print("enter 3 to update contact")
    print("enter 4 to read contact")
    print("enter 5 to exit")
    choice=int(input("enter your choice: "))
    if choice==1:
      print("create contact")
      id=int(input("enter id: "))
      name=input("enter name: ")
      phone=input("enter phone number: ")
      email=input("enter email: ")
      address=input("enter address: ")
      contactor.create_contact(id,name,phone,email,address)
    elif choice==2:
        print("delete contact")
        id=int(input("enter id to delete user data: "))
        contactor.delete_contact(id)
    elif choice==3:
        print("update contact")
        id=input("enter id to update: ")
        name=input("enter name to update: ")
        phone=input("enter new phone number: ")
        email=input("enter new email: ")
        address=input("enter new address: ")
        contactor.update_contact(id,name,phone,email,address)
    elif choice==4:
        contactor.read_contacts()
    elif choice==5:
        print("exit contact book")
        break
    else:
        print("invalid choice")
        