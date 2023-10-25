# Define the filename for the database file
database_file = "database.txt"

# Function to display the main menu
def display_menu():
    print("\n1. View Entries")
    print("2. Add Entry")
    print("3. Update Entry")
    print("4. Delete Entry")
    print("5. Exit")

# Function to view existing entries with serial numbers
def view_entries():
    try:
        with open(database_file, "r") as file:
            entries = file.readlines()
            if entries:
                print("Entries:")
                for i, entry in enumerate(entries, 1):
                    print(f"{i}. {entry.strip()}")
            else:
                print("No entries found.")
    except FileNotFoundError:
        print("Database file not found.")

# Function to add a new entry
def add_entry():
    name = input("Enter name: ")
    age = input("Enter age: ")
    new_entry = f"Name: {name}, Age: {age}\n"

    with open(database_file, "r") as file:
        entries = file.readlines()
        for entry in entries:
            if entry.strip() == new_entry.strip():
                print("Entry with the same name and age already exists.")
                return  # Exit the function if a duplicate entry is found
    
    with open(database_file, "a") as file:
        file.write(new_entry)
        print("Entry added successfully!")


# Function to update an existing entry
def update_entry():
    name_to_update = input("Enter the name to update: ")

    try:
        with open(database_file, "r") as file:
            entries = file.readlines()
        with open(database_file, "w") as file:
            entry_updated = False
            for entry in entries:
                if entry.startswith(f"Name: {name_to_update}"):
                    new_name = input("Enter the new name: ")
                    new_age = input("Enter the new age: ")
                    updated_entry = f"Name: {new_name}, Age: {new_age}\n"
                    file.write(updated_entry)
                    entry_updated = True

            if entry_updated:
                print("Entry updated successfully!")
            else:
                print(f"No entry found with the name: {name_to_update}")
    except FileNotFoundError:
        print("Database file not found.")


# Function to delete an entry
def delete_entry():
    name_to_delete = input("Enter the name to delete: ")

    try:
        with open(database_file, "r") as file:
            entries = file.readlines()
        with open(database_file, "w") as file:
            deleted = False
            for i, entry in enumerate(entries):
                if entry.startswith(f"Name: {name_to_delete}"):
                    deleted = True
                else:
                    file.write(entry)
            if deleted:
                print("Entry deleted successfully!")
            else:
                print("Entry not found.")
    except FileNotFoundError:
        print("Database file not found.")


# Main program

print("Welcome to the Basic File Manipulation Program!")

while True:
    display_menu()
    choice = input("\nSelect an option: ")

    if choice == "1":
        view_entries()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        update_entry()
    elif choice == "4":
        delete_entry()
    elif choice == "5":
        break
    else:
        print("Invalid option. Please select a valid option.")

print("Exiting the program.")
