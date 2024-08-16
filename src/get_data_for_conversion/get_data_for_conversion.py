import json

from src.get_data_for_conversion.send_conversion_request import send_conversion_request

DATA_FILE = 'data.json'

def get_data():
    """Fetch savings entries and goals from a JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return data.get('savings_entries', []), data.get('savings_goals', [])
    except FileNotFoundError:
        print(f"Error: The file {DATA_FILE} does not exist.")
        return [], []
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
        return [], []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], []

def display_options(options, option_type):
    """Display a list of options for the user to choose from."""
    print(f"\nAvailable {option_type}:")
    for idx, item in enumerate(options):
        print(f"{idx + 1}. {item}")

def get_user_choice(num_options, option_type):
    """Prompt the user to select an option from a list."""
    while True:
        try:
            choice = int(input(f"Select a {option_type} (number): ")) - 1
            if 0 <= choice < num_options:
                return choice
            else:
                print(f"Invalid selection. Please select a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_data_for_conversion():
    """Prompt the user to select a savings entry or goal and return the selected item."""
    entries, goals = get_data()

    print("\nWould you like to convert:")
    print("1. A Savings Entry")
    print("2. A Savings Goal")
    choice = input("Please select an option (1 or 2): ")

    if choice == '1':
        if not entries:
            print("No savings entries available.")
            return None
        display_options(entries, "savings entries")
        index = get_user_choice(len(entries), "savings entry")
        selected_entry = entries[index]
        print(f"Selected item for conversion: {selected_entry}")
        target_currency = get_target_currency()

        response = send_conversion_request(selected_entry['currency'], target_currency, selected_entry['amount'],
                                           override=False)
        if response:
            converted_amount = response.get('Value')
            if converted_amount is not None:
                selected_entry['amount'] = converted_amount
                selected_entry['currency'] = target_currency
                print(f"Conversion successful: {converted_amount} {target_currency}")
            else:
                print("Conversion failed.")
        else:
            print("Failed to get response from the conversion service.")

    elif choice == '2':
        if not goals:
            print("No savings goals available.")
            return None
        display_options(goals, "savings goals")
        index = get_user_choice(len(goals), "savings goal")
        selected_goal = goals[index]
        print(f"Selected item for conversion: {selected_goal}")
        target_currency = get_target_currency()

        response = send_conversion_request(selected_goal['currency'], target_currency, selected_goal['target_amount'],
                                           override=False)
        if response:
            converted_amount = response.get('Value')
            if converted_amount is not None:
                selected_goal['target_amount'] = converted_amount
                selected_goal['currency'] = target_currency
                print(f"Conversion successful: {converted_amount} {target_currency}")
            else:
                print("Conversion failed.")
        else:
            print("Failed to get response from the conversion service.")

    else:
        print("Invalid selection.")
        return None

    update_data_file(entries, goals)


def get_target_currency():
    target_currency = input("Enter the currency you want to convert to (e.g., EUR): ")
    return target_currency


def update_data_file(updated_entries, updated_goals):
    """Update the data.json file with the new entries and goals."""
    data = {
        "savings_entries": updated_entries,
        "savings_goals": updated_goals
    }

    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error updating data file: {e}")


# Example usage
if __name__ == "__main__":
    get_data_for_conversion()

