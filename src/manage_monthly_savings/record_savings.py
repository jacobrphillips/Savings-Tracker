import json
from datetime import datetime

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

def is_valid_date(date_str):
    """Check if the provided date string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def record_savings():
    """Record a new savings entry or cancel the operation."""
    data = load_data()

    print("\n---------------------------------")
    print("|        Record Savings          |")
    print("---------------------------------")

    display_goals(data.get('savings_goals', []))

    goal_index = input("Select the number of the goal this savings is for or type 'C' to cancel: ").strip()
    if goal_index.lower() == 'c':
        print("Operation canceled.")
        return

    try:
        goal_index = int(goal_index) - 1
        if not (0 <= goal_index < len(data['savings_goals'])):
            print("Invalid goal number. Operation canceled.")
            return

        selected_goal = data['savings_goals'][goal_index]
        goal_name = selected_goal.get('name', 'No Name')
        target_amount = selected_goal.get('target_amount', 0.00)
        print(f"Selected Goal: {goal_name} - Target Amount: ${target_amount:.2f}")

    except ValueError:
        print("Invalid input. Operation canceled.")
        return

    while True:
        date = input("Enter date (YYYY-MM-DD) or type 'C' to cancel: ").strip()
        if date.lower() == 'c':
            print("Operation canceled.")
            return
        if is_valid_date(date):
            break
        else:
            print("Invalid date format. Please use YYYY-MM-DD format.")

    while True:
        try:
            amount_input = input("Enter amount: $ or type 'C' to cancel: ").strip()
            if amount_input.lower() == 'c':
                print("Operation canceled.")
                return
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be positive. Please enter a valid amount.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value or 'C' to cancel.")

    save_option = input(f"\nSave entry: {date} - ${amount} for goal '{goal_name}'? (Y/N/C to cancel): ").strip().upper()
    if save_option == 'Y':
        data['savings_entries'].append({"date": date, "amount": amount, "goal_name": goal_name})
        save_data(data)
        print(f"\nRecorded ${amount:.2f} for {date} towards goal '{goal_name}'.")
    elif save_option == 'N':
        print("Entry not saved.")
    elif save_option == 'C':
        print("Operation canceled.")
    else:
        print("Invalid input. Entry not saved.")

# Wireframe:
# ---------------------------------
# |        Record Savings          |
# ---------------------------------
# | Available Goals:               |
# | 1. Save $500 by September      |
# | 2. Save $1000 by December      |
# ---------------------------------
# | Select the number of the goal  |
# | this savings is for or type    |
# | 'C' to cancel: _               |
# ---------------------------------
# | Enter date (YYYY-MM-DD) or     |
# | type 'C' to cancel: _          |
# ---------------------------------
# | Enter amount: $ or type 'C'    |
# | to cancel: _                   |
# ---------------------------------
# | Save entry: 2024-07-15 - $500  |
# | for goal 'Save $500 by         |
# | September'? (Y/N/C to cancel): |
# ---------------------------------
# | Recorded $500 for 2024-07-15   |
# | towards goal 'Save $500 by     |
# | September'.                    |
# ---------------------------------
