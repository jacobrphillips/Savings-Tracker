def back_to_main_menu():
    """Prompt the user to go back to the main menu."""
    while True:
        print("\n---------------------------------")
        print("|      Back to Main Menu?       |")
        print("---------------------------------")
        choice = input("Would you like to go back to the main menu? [Y/N]: ").strip().lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            break
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")