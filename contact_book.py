menu = """========== CONTACT BOOK ==========

1. Add Contact
2. Search Contact
3. View Contacts
4. Exit"""

contacts = {
    "users":[

    ]
}

def add_contact():
  name = input("Enter your name:")
  num = int(input("Enter your number:"))
  email = input("Enter your email:")
  contacts["users"].append({"name":name,"number":num,"email":email})

def search_contact():
  search = input("Enter the name to search:")
  found = False
  for i in contacts["users"]:
    if search in i["name"]:
      print("Name:",i["name"])
      print("Number:",i["number"])
      print("Email:",i["email"])
      found = True
  if found is False:
    print("Contact not found")

def view_contact():
  for i in contacts["users"]:
    print("***All Saved Contacts***")
    print("Name:",i["name"])
    print("Number:",i["number"])
    print("Email:",i["email"])

choice = 0
while choice != 4:
  print(menu)
  choice = int(input("Enter your choice:"))
  if choice == 1:
    add_contact()
  elif choice == 2:
    search_contact()
  elif choice == 3:
    view_contact()
  elif choice == 4:
    print("Exit!")
  else:
    print("Invalid choice.")
