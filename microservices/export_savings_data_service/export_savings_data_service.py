import csv
import io
import json
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

DATA_FILE_PATH = '../../src/data.json'

def read_existing_data():
    """Reads existing data from data.json."""
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"savings_entries": [], "savings_goals": []}
    except json.JSONDecodeError:
        return {"savings_entries": [], "savings_goals": []}

def write_data(data):
    """Writes the data to data.json."""
    with open(DATA_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/export-savings-data', methods=['GET'])
def export_savings_data_service():
    try:
        data = read_existing_data()
        savings_entries = data.get("savings_entries", [])

        # Create a CSV in memory
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=['Date', 'Amount', 'Name', 'Currency'])
        writer.writeheader()
        for entry in savings_entries:
            writer.writerow({
                'Date': entry['date'],
                'Amount': entry['amount'],
                'Name': entry['goal_name'],
                'Currency': entry['currency']
            })
        output.seek(0)  # Move to the beginning of the StringIO buffer

        # Send the CSV as a response
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            download_name="export_savings_data.csv",
            mimetype="text/csv"
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5002)
