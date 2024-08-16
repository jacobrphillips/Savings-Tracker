import requests
import os

def export_savings_data():
    prompt = input("Are you sure you want to export your savings data? (Y/N): ").strip().upper()

    if prompt == 'Y':
        try:
            response = requests.get("http://localhost:5002/export-savings-data", stream=True)

            if response.status_code == 200:
                try:
                    with open('export_savings_data.csv', 'wb') as f:
                        f.write(response.content)
                        f.flush()
                        os.fsync(f.fileno())
                    print("Data exported and written to export_savings_data.csv successfully.")
                except Exception as file_write_error:
                    print(f"Error writing to file: {file_write_error}")
            else:
                try:
                    error_message = response.json().get("error", "Unknown error")
                except ValueError:
                    error_message = response.text
                print("Failed to export data:", error_message)
        except Exception as request_error:
            print(f"Error exporting data: {request_error}")
    elif prompt == 'N':
        print("Export operation cancelled.")
    else:
        print("Invalid choice. Please enter 'Y' for Yes or 'N' for No.")

if __name__ == "__main__":
    export_savings_data()
