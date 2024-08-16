import sys
import requests
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image


def savings_trends_analysis():
    year = input("Enter the year for savings trend analysis (e.g., 2023): ").strip()

    try:
        response = requests.get(f"http://localhost:5004/savings-trends?year={year}", stream=True)

        if response.status_code == 200:
            graph_filename = f"savings_trends_analysis_{year}.png"
            with open(graph_filename, 'wb') as f:
                f.write(response.content)
            print(f"Graph saved as {graph_filename}")
            img = Image.open(BytesIO(response.content))
            plt.imshow(img)
            plt.axis('off')
            plt.title(f'Savings Trends for {year}')
            plt.show()
        else:
            print("Failed to retrieve savings trends:", response.json().get("error", "Unknown error"))

    except Exception as e:
        print("Error while retrieving savings trends:", e)