import json
from .view_detailed_entry import view_detailed_entry
from .list_all_entries import list_all_entries
from src.back_to_main_menu import back_to_main_menu

DATA_FILE = 'data.json'


def load_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def view_savings_history():
    while True:
        print("\n---------------------------------")
        print("|      View Savings History      |")
        print("---------------------------------")
        print("| 1. List All Entries            |")
        print("| 2. View Detailed Entry         |")
        print("| 3. Back to Main Menu           |")
        print("---------------------------------")
        choice = input("Select an option: ")

        if choice == '1':
            list_all_entries()
        elif choice == '2':
            view_detailed_entry()
        elif choice == '3':
            if back_to_main_menu():
                return
        else:
            print("Invalid choice, please try again.")
