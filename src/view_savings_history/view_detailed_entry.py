import json

DATA_FILE = 'data.json'


def load_data():
    """Load data from the JSON file."""
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


def view_detailed_entry():
    """View a detailed savings entry."""
    data = load_data()

    if not data['savings_entries']:
        print("\n---------------------------------")
        print("|   No entries available.        |")
        print("---------------------------------")
        return

    if not data['savings_goals']:
        print("\n---------------------------------")
        print("|   No goals available.          |")
        print("---------------------------------")

    while True:
        print("\n---------------------------------")
        print("|   Existing Savings Entries     |")
        print("---------------------------------")
        for i, entry in enumerate(data['savings_entries']):
            print(f"| {i + 1}. {entry['date']} - ${entry['amount']:,.2f} |")
        print("---------------------------------")

        try:
            entry_input = input("Select an entry to view details (or 'B' to go back): ").strip().lower()

            if entry_input == 'b':
                print("\nReturning to View Savings History...")
                return

            entry_id = int(entry_input) - 1

            if 0 <= entry_id < len(data['savings_entries']):
                entry = data['savings_entries'][entry_id]
                goal_name = entry.get('goal_name', 'No Goal')

                # Find the associated goal
                goal = next((g for g in data['savings_goals'] if g['name'] == goal_name), None)
                goal_target_amount = goal.get('target_amount', 0.00) if goal else 0.00

                print("\n---------------------------------")
                print("|          Detailed Entry        |")
                print("---------------------------------")
                print(f"| Date: {entry['date']}          |")
                print(f"| Amount: ${entry['amount']:,.2f} |")
                print(f"| Goal: {goal_name}             |")
                print(f"| Goal Target Amount: ${goal_target_amount:,.2f} |")
                print("---------------------------------")

                return_to_menu = input(
                    "Would you like to return to the View Savings History menu? [Y/N]: ").strip().lower()

                if return_to_menu == 'y':
                    print("\nReturning to View Savings History...")
                    return
                elif return_to_menu == 'n':
                    print("\nSelecting another entry...")
                else:
                    print("Invalid choice. Exiting detailed view...")
                    return
            else:
                print("\nInvalid entry ID.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
