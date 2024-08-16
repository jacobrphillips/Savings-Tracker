import sys

from src.get_data_for_conversion.get_data_for_conversion import get_data_for_conversion
from src.manage_monthly_savings.manage_monthly_savings import manage_monthly_savings
from src.view_savings_history.view_savings_history import view_savings_history
from src.set_savings_goal.set_savings_goal import set_savings_goal
from src.import_savings_data.import_savings_data import import_savings_data
from src.export_savings_data.export_savings_data import export_savings_data
from src.savings_trends_analysis.savings_trends_analysis import savings_trends_analysis


def display_main_menu():
    print("\n---------------------------------")
    print("|        Savings Tracker         |")
    print("---------------------------------")
    print("| 1. Manage Monthly Savings      |")
    print("| 2. View Savings History        |")
    print("| 3. Set Savings Goal            |")
    print("| 4. Import Savings Data         |")
    print("| 5. Export Savings Data         |")
    print("| 6. Savings Trend Analysis      |")
    print("| 7. Currency Conversion         |")
    print("| 8. Exit                        |")
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
            import_savings_data()
        elif choice == '5':
            export_savings_data()
        elif choice == '6':
            savings_trends_analysis()
        elif choice == '7':
            get_data_for_conversion()
        elif choice == '8':
            print("Exiting the application.")
            sys.exit()
        else:
            print("\n***Invalid choice, please try again.***")


if __name__ == "__main__":
    main()
