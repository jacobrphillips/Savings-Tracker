import requests

def send_conversion_request(detect_currency, target_currency, value, override):
    """Send a currency conversion request and return the response."""
    currency_request = {
        "Detect": detect_currency,
        "Target": target_currency,
        "Value": value,
        "Override": override
    }

    try:
        response = requests.post('http://127.0.0.1:5001/convert-currency', json=currency_request)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return None
