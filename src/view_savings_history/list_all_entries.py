import json
from .view_detailed_entry import view_detailed_entry

DATA_FILE = 'data.json'

def load_data():
    """Load data from the JSON file."""
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def list_all_entries():
    """List all savings entries and provide an option to view details."""
    data = load_data()
    print("\n---------------------------------")
    print("|       Savings History          |")
    print("---------------------------------")

    if not data['savings_entries']:
        print("| No entries available.         |")
    else:
        for i, entry in enumerate(data['savings_entries']):
            print(f"| {i + 1}. {entry['date']} - ${entry['amount']:,.2f} |")

    print("---------------------------------")

    while True:
        view_details = input("Would you like to view details for any entry? [Y/N]: ").strip().lower()
        if view_details == 'n':
            print("\nReturning to the previous menu...")
            return
        elif view_details == 'y':
            try:
                view_detailed_entry()
                return
            except ValueError:
                print("\nInvalid input. Please enter a number.")
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
