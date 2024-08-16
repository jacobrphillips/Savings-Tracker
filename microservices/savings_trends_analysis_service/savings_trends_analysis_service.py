import os
import csv
import io
import json
import datetime
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

DATA_FILE_PATH = '../../src/data.json'
GRAPH_FILE_PATH = '../../savings_trends_analysis_{}.png'

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

@app.route('/savings-trends', methods=['GET'])
def savings_trends_analysis_service():
    year = request.args.get('year')
    if not year:
        return jsonify({"error": "Year parameter is required"}), 400

    try:
        data = read_existing_data()
        savings_entries = data.get("savings_entries", [])

        # Filter entries for the specified year and aggregate by month
        monthly_savings = [0] * 12
        for entry in savings_entries:
            entry_date = datetime.datetime.strptime(entry['date'], '%Y-%m-%d')
            if entry_date.year == int(year):
                monthly_savings[entry_date.month - 1] += float(entry['amount'])

        # Generate the graph
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        plt.figure(figsize=(10, 6))
        plt.plot(months, monthly_savings, marker='o')
        plt.title(f'Savings Trends for {year}')
        plt.xlabel('Month')
        plt.ylabel('Total Savings')
        plt.grid(True)
        plt.tight_layout()

        # Save the plot to a file
        graph_filename = GRAPH_FILE_PATH.format(year)
        plt.savefig(graph_filename)
        plt.close()

        return send_file(graph_filename, mimetype='image/png', as_attachment=True, download_name=graph_filename)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5004)
