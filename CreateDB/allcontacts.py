import sqlite3

db = sqlite3.connect("contacts.sqlite")
name = input("Please enter the name to search for ")

# for name, phone, email in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
for name, phone, email in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()