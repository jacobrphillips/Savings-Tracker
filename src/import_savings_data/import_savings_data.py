import requests
import json

def import_savings_data():
    file_path = input("Enter the path to the CSV file to import: ")
    with open(file_path, 'rb') as file:
        response = requests.post("http://localhost:5003/import-savings-data", files={"file": file})
        if response.ok:
            # Parse the response JSON
            response_data = response.json()
            if response_data.get("status") == "success":
                print("Data imported and written to data.json successfully.")
            else:
                print("Failed to import data:", response_data.get("error", "Unknown error"))
        else:
            print("Failed to import data:", response.text)

if __name__ == "__main__":
    import_savings_data()
