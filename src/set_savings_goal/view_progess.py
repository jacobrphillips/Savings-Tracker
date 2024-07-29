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

def calculate_progress(goal_name, savings_entries):
    """Calculate progress towards a specific goal."""
    total_savings = 0
    for entry in savings_entries:
        if entry.get('goal_name') == goal_name:
            total_savings += entry['amount']
    return total_savings

def display_goals_and_progress(goals, savings_entries):
    """Display the current goals and their progress."""
    print("\n---------------------------------")
    print("|          View Progress         |")
    print("---------------------------------")
    print("| Current Goals and Progress:    |")

    if not goals:
        print("| No goals available.            |")
    else:
        for i, goal in enumerate(goals):
            name = goal.get('name', 'No Name')
            target_amount = goal.get('target_amount', 0.00)
            progress = calculate_progress(name, savings_entries)

            if target_amount > 0:
                progress_percentage = (progress / target_amount) * 100
            else:
                progress_percentage = 0

            if progress_percentage >= 100:
                status = "[Completed]"
            elif progress > 0:
                status = f"[In Progress: ${progress:.2f} saved]"
            else:
                status = "[Not Started]"

            print(f"| {i + 1}. {name:<30} | {status:<30} |")

    print("---------------------------------")

def view_progress():
    """View progress towards savings goals."""
    data = load_data()

    while True:
        display_goals_and_progress(data['savings_goals'], data['savings_entries'])

        print("\n---------------------------------")
        print("| Options:                       |")
        print("| 1. View Detailed Progress      |")
        print("| 2. Update Progress             |")
        print("| 3. Delete Goal                 |")
        print("| 4. Back to Set Goals Menu      |")
        print("---------------------------------")

        choice = input("Select an option: ").strip()

        if choice == '1':
            view_detailed_progress()
        elif choice == '2':
            update_progress()
        elif choice == '3':
            delete_goal()
        elif choice == '4':
            print("Returning to the Set Savings Goals menu.")
            return
        else:
            print("\n***Invalid choice, please try again.***")


def view_detailed_progress():
    """View detailed progress for a specific goal."""
    data = load_data()
    if not data['savings_goals']:
        print("\nNo savings goals available.")
        return

    print("\n---------------------------------")
    print("|     Select a Goal to View      |")
    print("---------------------------------")

    for i, goal in enumerate(data['savings_goals']):
        print(f"{i + 1}. {goal.get('name', 'No Name')}")

    try:
        goal_index = int(input("Select a goal number: ")) - 1
        if 0 <= goal_index < len(data['savings_goals']):
            goal = data['savings_goals'][goal_index]
            name = goal.get('name', 'No Name')
            target_amount = goal.get('target_amount', 0.00)
            progress = calculate_progress(name, data['savings_entries'])
            progress_percentage = (progress / target_amount) * 100 if target_amount > 0 else 0

            print("\n---------------------------------")
            print(f"| Detailed Progress for {name} |")
            print("---------------------------------")
            print(f"| Target Amount: ${target_amount:.2f} |")
            print(f"| Amount Saved: ${progress:.2f}        |")
            print(f"| Progress: {progress_percentage:.2f}%   |")

            if progress_percentage >= 100:
                print("| Status: [Completed]            |")
            elif progress > 0:
                print(f"| Status: [In Progress: ${progress:.2f} saved] |")
            else:
                print("| Status: [Not Started]          |")

            print("---------------------------------")
        else:
            print("\nInvalid goal number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")


def update_progress():
    """Update progress by adding a new savings entry."""
    data = load_data()
    if not data['savings_goals']:
        print("\nNo savings goals available.")
        return

    print("\n---------------------------------")
    print("|     Select a Goal to Update    |")
    print("---------------------------------")

    for i, goal in enumerate(data['savings_goals']):
        print(f"{i + 1}. {goal.get('name', 'No Name')}")

    try:
        goal_index = int(input("Select a goal number: ")) - 1
        if 0 <= goal_index < len(data['savings_goals']):
            goal = data['savings_goals'][goal_index]
            goal_name = goal.get('name', 'No Name')

            while True:
                print("\n---------------------------------")
                print("|     Update Progress            |")
                print("| 1. Add New Entry               |")
                print("| 2. Cancel                      |")
                print("---------------------------------")
                option = input("Select an option: ").strip()

                if option == '1':
                    try:
                        amount = float(input(f"Enter amount saved for goal '{goal_name}': $"))
                        if amount <= 0:
                            print("Amount must be positive. Please try again.")
                            continue

                        date = input("Enter date (YYYY-MM-DD): ")

                        new_entry = {
                            'date': date,
                            'amount': amount,
                            'goal_name': goal_name
                        }

                        data['savings_entries'].append(new_entry)
                        save_data(data)

                        print(f"\nAdded ${amount:.2f} to goal '{goal_name}'.")

                        return
                    except ValueError:
                        print("Invalid amount. Please enter a numeric value.")
                elif option == '2':
                    print("Canceling update.")
                    return
                else:
                    print("\n***Invalid choice, please try again.***")
        else:
            print("\nInvalid goal number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")


def delete_goal():
    """Delete a specific goal."""
    data = load_data()

    if not data['savings_goals']:
        print("\nNo goals available to delete.")
        return

    print("\n---------------------------------")
    print("|        Delete a Goal           |")
    print("---------------------------------")

    # Display goals with numbers
    for i, goal in enumerate(data['savings_goals']):
        name = goal.get('name', 'No Name')
        print(f"{i + 1}. {name}")

    print("\n---------------------------------")
    print("| Enter 'c' to cancel.           |")
    print("---------------------------------")

    try:
        goal_selection = input("Select a goal number to delete or 'c' to cancel: ").strip().lower()

        if goal_selection == 'c':
            print("Cancellation complete. Returning to progress menu.")
            return

        goal_index = int(goal_selection) - 1
        if 0 <= goal_index < len(data['savings_goals']):
            goal = data['savings_goals'][goal_index]
            goal_name = goal.get('name', 'No Name')

            print("\n---------------------------------")
            print("| Note: Deleting this goal will  |")
            print("| remove it permanently.         |")
            print("| Are you sure you want to delete? |")
            print("| 1. Confirm                    |")
            print("| 2. Cancel                     |")
            print("---------------------------------")
            proceed = input("Select an option: ").strip()

            if proceed == '1':
                del data['savings_goals'][goal_index]
                data['savings_entries'] = [entry for entry in data['savings_entries'] if
                                           entry.get('goal_name') != goal_name]
                save_data(data)
                print(f"Goal '{goal_name}' has been deleted.")
                return
            elif proceed == '2':
                print("Deletion canceled.")
                return
            else:
                print("Invalid selection. Deletion canceled.")
                return
        else:
            print("Invalid goal number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
