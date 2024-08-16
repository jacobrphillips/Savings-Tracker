import requests
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv('API_KEY')


@app.route('/convert-currency', methods=['POST'])
def convert_currency():
    """Handle currency conversion requests."""
    try:
        data = request.get_json()
        detect_currency = data['Detect']
        target_currency = data['Target']
        value = data['Value']
        override = data.get('Override', None)

        if override:
            exchange_rate = override
        else:
            url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{detect_currency}'
            response = requests.get(url)
            response.raise_for_status()
            response_data = response.json()
            exchange_rate = response_data['conversion_rates'].get(target_currency)

            if exchange_rate is None:
                return jsonify({"Error": "Conversion rate not found"}), 404

        converted_value = value * exchange_rate
        return jsonify({
            "Value": round(converted_value, 2),
            "Conversion_rate": round(exchange_rate, 2),
            "Error": False
        })

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5001)
