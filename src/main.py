import sys
from src.manage_monthly_savings.manage_monthly_savings import manage_monthly_savings
from src.view_savings_history.view_savings_history import view_savings_history
from src.set_savings_goal.set_savings_goal import set_savings_goal


def display_main_menu():
    print("\n---------------------------------")
    print("|        Savings Tracker         |")
    print("---------------------------------")
    print("| 1. Manage Monthly Savings      |")
    print("| 2. View Savings History        |")
    print("| 3. Set Savings Goal            |")
    print("| 4. Exit                        |")
    print("---------------------------------")
    choice = input("Please select an option: ")
    return choice


def main():
    while True:
        choice = display_main_menu()

        if choice == '1':
            manage_monthly_savings()
        elif choice == '2':
            view_savings_history()
        elif choice == '3':
            set_savings_goal()
        elif choice == '4':
            print("Exiting the application.")
            sys.exit()
        else:
            print("\n***Invalid choice, please try again.***")


if __name__ == "__main__":
    main()
