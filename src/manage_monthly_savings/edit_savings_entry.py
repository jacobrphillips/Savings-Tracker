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


def display_goals(goals):
    """Display available goals for selection."""
    if not goals:
        print("No goals available.")
        return

    print("\nAvailable Goals:")
    for i, goal in enumerate(goals):
        print(f"{i + 1}. {goal.get('name', 'No Name')} - Target: ${goal.get('target_amount', 0.00):.2f}")


def edit_savings_entry():
    """Edit an existing savings entry."""
    data = load_data()

    if not data['savings_entries']:
        print("\nNo savings entries available to edit.")
        return

    print("\n---------------------------------")
    print("|        Edit Savings Entry      |")
    print("---------------------------------")

    for i, entry in enumerate(data['savings_entries']):
        goal_name = entry.get('goal_name', 'No Goal')
        print(f"| {i + 1}. {entry['date']} - ${entry['amount']} (Goal: {goal_name}) |")
    print("---------------------------------")

    try:
        entry_id = int(input("Select an entry to edit: ")) - 1
        if 0 <= entry_id < len(data['savings_entries']):
            print("\n---------------------------------")
            print("| Note: Editing this entry will  |")
            print("| overwrite the existing amount. |")
            print("| Are you sure you want to edit? |")
            print("---------------------------------")
            proceed = input("Proceed? [Y/N] ").lower()

            if proceed == 'y':
                new_amount = float(input("Enter new amount: "))

                print("\nWould you like to change the goal for this entry?")

                confirm = input("Save changes? [Y/N] ").lower()

                if confirm == 'y':
                    data['savings_entries'][entry_id]['amount'] = new_amount
                    save_data(data)
                    print("Changes saved.")
                else:
                    print("Changes not saved.")
            else:
                print("Edit canceled.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Wireframe:
# ---------------------------------
# |        Edit Savings Entry      |
# ---------------------------------
# | 1. 2024-07-15 - $500 (Goal:    |
# |    Save $500 by September)     |
# | 2. 2024-07-14 - $600 (Goal:    |
# |    Save $1000 by December)     |
# | ...                            |
# ---------------------------------
# Select an entry to edit: _
# ---------------------------------
# | Note: Editing this entry will  |
# | overwrite the existing amount. |
# | Are you sure you want to edit? |
# ---------------------------------
# Proceed? [Y/N] _
# ---------------------------------
# Enter new amount: _
# ---------------------------------
# Would you like to change the goal |
# for this entry?                  |
# Available Goals:                 |
# 1. Save $500 by September        |
# 2. Save $1000 by December        |
# Select a new goal number or type  |
# '0' to keep the current goal: _  |
# ---------------------------------
# Save changes? [Y/N] _
