import csv
import io
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Update this path as needed
DATA_FILE_PATH = '../../src/data.json'

def read_existing_data():
    """Reads existing data from data.json."""
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            data = json.load(f)
        print("Existing data loaded:", data)
        return data
    except FileNotFoundError:
        print("data.json not found. Creating new data file.")
        return {"savings_entries": [], "savings_goals": []}
    except json.JSONDecodeError:
        print("Error decoding JSON. Returning empty data.")
        return {"savings_entries": [], "savings_goals": []}

def write_data(data):
    """Writes the data to data.json."""
    with open(DATA_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data written to data.json")

@app.route('/import-savings-data', methods=['POST'])
def import_savings_data_service():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.csv'):
        try:
            data = csv.DictReader(io.StringIO(file.stream.read().decode("UTF8"), newline=None))
            existing_data = read_existing_data()
            goal_amounts = {}

            for row in data:
                entry = {
                    "date": row['Date'],
                    "amount": float(row['Amount']),
                    "goal_name": row['Name'],
                    "currency": "USD"
                }
                existing_data["savings_entries"].append(entry)

                if entry["goal_name"] in goal_amounts:
                    if entry["amount"] > goal_amounts[entry["goal_name"]]:
                        goal_amounts[entry["goal_name"]] = entry["amount"]
                else:
                    goal_amounts[entry["goal_name"]] = entry["amount"]

            for goal_name, target_amount in goal_amounts.items():

                existing_goal = next((g for g in existing_data["savings_goals"] if g["name"] == goal_name), None)
                if existing_goal:

                    if target_amount > existing_goal["target_amount"]:
                        existing_goal["target_amount"] = target_amount
                        existing_goal["currency"] = "USD"
                else:
                    # Add new goal
                    existing_data["savings_goals"].append({
                        "name": goal_name,
                        "target_amount": target_amount,
                        "currency": "USD"
                    })

            write_data(existing_data)

            return jsonify({"status": "success", "message": "Data imported successfully."})
        except Exception as e:
            print("Error processing file:", e)  # Debugging print
            return jsonify({"error": "Error processing file."}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a CSV file."}), 400

if __name__ == '__main__':
    app.run(port=5003)
