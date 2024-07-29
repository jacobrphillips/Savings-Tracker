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


def edit_existing_goal():
    """Edit an existing savings goal."""
    data = load_data()

    if not data['savings_goals']:
        print("\n---------------------------------")
        print("|   No goals available to edit.  |")
        print("---------------------------------")
        return

    print("\n---------------------------------")
    print("|     Existing Savings Goals     |")
    print("---------------------------------")
    for i, goal in enumerate(data['savings_goals']):
        name = goal.get('name', 'No Name')
        target_amount = goal.get('target_amount', 0.00)
        print(f"| {i + 1}. {name} - ${target_amount:.2f} |")
    print("---------------------------------")

    while True:
        try:
            goal_id = int(input("Select a goal to edit: ")) - 1
            if 0 <= goal_id < len(data['savings_goals']):
                goal = data['savings_goals'][goal_id]

                new_name = input("Enter new goal name: ")
                while True:
                    try:
                        new_target_amount = float(input("Enter new target amount: $"))
                        break
                    except ValueError:
                        print("Invalid amount. Please enter a numeric value.")

                # Update goal
                data['savings_goals'][goal_id] = {"name": new_name, "target_amount": new_target_amount}
                save_data(data)
                print("Goal updated.")
                return
            else:
                print("Invalid goal ID.")
        except ValueError:
            print("Invalid input. Please enter a number.")
