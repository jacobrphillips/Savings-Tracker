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


def create_new_goal():
    """Create a new savings goal."""
    data = load_data()

    print("\n---------------------------------")
    print("|         Create New Goal        |")
    print("---------------------------------")
    goal_name = input("Enter goal name: ")

    while True:
        try:
            target_amount = float(input("Enter target amount: $"))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    save_option = input(f"\nSave goal: {goal_name} - ${target_amount}? (Y/N): ").strip().upper()
    if save_option == 'Y':
        data['savings_goals'].append({"name": goal_name, "target_amount": target_amount})
        save_data(data)
        print(f"\nSaved goal '{goal_name}' with target amount ${target_amount}.")
    else:
        print("Goal not saved.")
        return
