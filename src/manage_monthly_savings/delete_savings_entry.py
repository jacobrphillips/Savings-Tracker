import json


DATA_FILE = 'data.json'


def load_data():
    """Load data from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"savings_entries": [], "savings_goals": []}


def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def delete_savings_entry():
    """Delete an existing savings entry."""
    data = load_data()

    print("\n---------------------------------")
    print("|       Delete Savings Entry     |")
    print("---------------------------------")

    if not data['savings_entries']:
        print("No savings entries available to delete.")
        print("---------------------------------")
        return

    for i, entry in enumerate(data['savings_entries']):
        print(f"| {i + 1}. {entry['date']} - ${entry['amount']}          |")
    print("---------------------------------")

    print("\n** WARNING: Deleting an entry is irreversible. Once deleted, the entry cannot be recovered. **\n")
    print("---------------------------------")

    while True:
        try:
            entry_input = input("Select an entry to delete (or 'C' to cancel): ").strip().lower()
            if entry_input == 'c':
                print("Deletion process canceled.")
                return

            entry_id = int(entry_input) - 1
            if 0 <= entry_id < len(data['savings_entries']):
                print("\n---------------------------------")
                confirm = input("Confirm deletion? [Y/N/C to cancel]: ").strip().lower()

                if confirm == 'y':
                    del data['savings_entries'][entry_id]
                    save_data(data)
                    print("Entry deleted.")
                    return
                elif confirm == 'n' or confirm == 'c':
                    print("Deletion canceled.")
                    return
                else:
                    print("Invalid input. Please enter 'Y', 'N', or 'C'.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number or 'C' to cancel.")

# Wireframe:
# ---------------------------------
# |       Delete Savings Entry     |
# ---------------------------------
# | 1. 2024-07-15 - $500          |
# | 2. 2024-07-14 - $600          |
# | 3. 2024-07-13 - $450          |
# | ...                           |
# ---------------------------------
# ** WARNING: Deleting an entry is irreversible. Once deleted, the entry cannot be recovered. **
# ---------------------------------
# Select an entry to delete (or 'C' to cancel): _
# ---------------------------------
# Confirm deletion? [Y/N/C to cancel]: _
