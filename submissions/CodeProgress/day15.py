import json

def add_password():
    website = input("Enter name of website: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    entry = {"Website": website, "Email": email, "Password": password}
    save_entry(entry)
    print("Entry added successfully.")

def save_entry(entry):
    with open("passwords.json", "a") as file:
        json.dump(entry, file)
        file.write("\n")

def view_all():
    with open("passwords.json", "r") as file:
        for line in file:
            entry = json.loads(line)
            print_entry(entry)

def print_entry(entry):
    print("Website:", entry["Website"])
    print("\tEmail:", entry["Email"])
    print("\tPassword:", entry["Password"])

def search_entry():
    website = input("Enter the name of the website to search for: ")
    with open("passwords.json", "r") as file:
        for line in file:
            entry = json.loads(line)
            if entry["Website"].lower() == website.lower():
                print_entry(entry)

def delete_entry():
    website = input("Enter the name of the website to delete: ")
    with open("passwords.json", "r") as file:
        entries = [json.loads(line) for line in file]
    with open("passwords.json", "w") as file:
        for entry in entries:
            if entry["Website"].lower() != website.lower():
                json.dump(entry, file)
                file.write("\n")
    print("Entry deleted successfully.")

def update_entry():
    website = input("Enter the name of the website to update: ")
    new_password = input("Enter the new password: ")
    with open("passwords.json", "r") as file:
        entries = [json.loads(line) for line in file]
    with open("passwords.json", "w") as file:
        for entry in entries:
            if entry["Website"].lower() == website.lower():
                entry["Password"] = new_password
            json.dump(entry, file)
            file.write("\n")
    print("Entry updated successfully.")

def main():
    while True:
        print("\n1. Add a Password, Email, and Name of Website.")
        print("2. View all inputs")
        print("3. Search for a specific input")
        print("4. Delete an existing input")
        print("5. Update a specific input")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            update_entry()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()