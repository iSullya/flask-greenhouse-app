from flask import Flask, render_template
import csv
from collections import defaultdict

app = Flask(__name__)

# Function to read the latest data for each injection point
def read_latest_sensor_data():
    data = defaultdict(list)
    with open('sensor_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["timestamp"] = int(row["timestamp"])
            row["location"] = int(row["location"])
            row["pH"] = float(row["pH"])
            row["humidity"] = int(row["humidity"])
            row["temperature"] = float(row["temperature"])
            row["conductivity"] = int(row["conductivity"])
            row["nitrogen"] = int(row["nitrogen"])
            row["phosphorus"] = int(row["phosphorus"])
            row["potassium"] = int(row["potassium"])
            data[row["location"]].append(row)

    latest_data = []
    for location, records in data.items():
        latest_record = sorted(records, key=lambda x: x["timestamp"], reverse=True)[0]
        latest_record["label"] = f"P{location}"  # Add label for visualization
        latest_data.append(latest_record)

    return latest_data

# Function to read all historical data grouped by location
def read_historical_data():
    data = defaultdict(list)
    with open('sensor_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["timestamp"] = int(row["timestamp"])
            row["location"] = int(row["location"])
            row["pH"] = float(row["pH"])
            row["humidity"] = int(row["humidity"])
            row["temperature"] = float(row["temperature"])
            row["conductivity"] = int(row["conductivity"])
            row["nitrogen"] = int(row["nitrogen"])
            row["phosphorus"] = int(row["phosphorus"])
            row["potassium"] = int(row["potassium"])
            data[f"P{row['location']}"].append(row)  # Group by location (P1, P2, etc.)
    return data

@app.route('/')
def home():
    # Fetch the latest data and historical data
    injection_points = read_latest_sensor_data()
    historical_data = read_historical_data()

    # Pass data to the template
    return render_template('index.html', injection_points=injection_points, historical_data=historical_data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
