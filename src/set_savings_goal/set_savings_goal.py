from src.set_savings_goal.create_new_goal import create_new_goal
from src.set_savings_goal.edit_existing_goal import edit_existing_goal
from src.set_savings_goal.view_progess import view_progress
from src.back_to_main_menu import back_to_main_menu
import json

DATA_FILE = 'data.json'


def load_data():
    """Load data from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'savings_entries': [], 'savings_goals': []}


def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def set_savings_goal():
    """Main menu for setting savings goals."""
    while True:
        print("\n---------------------------------")
        print("|         Set Savings Goal       |")
        print("---------------------------------")
        print("| 1. Create New Goal             |")
        print("| 2. Edit Existing Goal          |")
        print("| 3. View Progress               |")
        print("| 4. Back to Main Menu           |")
        print("---------------------------------")
        choice = input("Select an option: ").strip()

        if choice == '1':
            create_new_goal()
        elif choice == '2':
            edit_existing_goal()
        elif choice == '3':
            view_progress()
        elif choice == '4':
            if back_to_main_menu():
                return
        else:
            print("\n***Invalid choice, please try again.***")

# Wireframe
# ---------------------------------
# |         Set Savings Goal       |
# ---------------------------------
# | 1. Create New Goal             |
# | 2. Edit Existing Goal          |
# | 3. View Progress               |
# | 4. Back to Main Menu           |
# ---------------------------------
# Select an option: _
