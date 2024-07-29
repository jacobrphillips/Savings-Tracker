import json
from .record_savings import record_savings
from .edit_savings_entry import edit_savings_entry
from .delete_savings_entry import delete_savings_entry
from src.back_to_main_menu import back_to_main_menu


DATA_FILE = 'data.json'


def load_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def manage_monthly_savings():
    while True:
        print("\n---------------------------------")
        print("|      Manage Monthly Savings    |")
        print("---------------------------------")
        print("| 1. Record Savings              |")
        print("| 2. Edit Savings Entry          |")
        print("| 3. Delete Savings Entry        |")
        print("| 4. Back to Main Menu           |")
        print("---------------------------------")
        choice = input("Select an option: ")

        if choice == '1':
            record_savings()
        elif choice == '2':
            edit_savings_entry()
        elif choice == '3':
            delete_savings_entry()
        elif choice == '4':
            if back_to_main_menu():
                return
        else:
            print("Invalid choice, please try again.")
