import csv
import random
from datetime import datetime, timedelta

def generate_sensor_data():
    # Define medians for the parameters
    medians = {
        "pH": 6.8,
        "humidity": 50,  # Percentage
        "temperature": 25,  # Celsius
        "conductivity": 1500,  # µS/cm
        "nitrogen": 360,  # mg/kg
        "phosphorus": 16.5,  # mg/kg
        "potassium": 195,  # mg/kg
    }

    # Define ranges of variation around the median
    variations = {
        "pH": 0.7,
        "humidity": 9,
        "temperature": 6,
        "conductivity": 500,
        "nitrogen": 70,
        "phosphorus": 7,
        "potassium": 50,
    }

    # Start timestamp (December 1, 2024) and locations
    start_date = datetime(2024, 12, 1)
    locations = list(range(1, 11))  # 10 locations

    # Generate 30 days of data for each location
    rows = []
    for day in range(30):  # Loop over days
        current_date = start_date + timedelta(days=day)
        timestamp = int(current_date.timestamp())

        for location in locations:
            row = {
                "timestamp": timestamp,
                "location": location,
                "pH": round(random.uniform(medians["pH"] - variations["pH"], medians["pH"] + variations["pH"]), 2),
                "humidity": round(random.uniform(medians["humidity"] - variations["humidity"], medians["humidity"] + variations["humidity"])),
                "temperature": round(random.uniform(medians["temperature"] - variations["temperature"], medians["temperature"] + variations["temperature"]), 1),
                "conductivity": round(random.uniform(medians["conductivity"] - variations["conductivity"], medians["conductivity"] + variations["conductivity"])),
                "nitrogen": round(random.uniform(medians["nitrogen"] - variations["nitrogen"], medians["nitrogen"] + variations["nitrogen"])),
                "phosphorus": round(random.uniform(medians["phosphorus"] - variations["phosphorus"], medians["phosphorus"] + variations["phosphorus"])),
                "potassium": round(random.uniform(medians["potassium"] - variations["potassium"], medians["potassium"] + variations["potassium"])),
            }
            rows.append(row)

    # Write rows to sensor_data.csv
    with open("sensor_data.csv", mode="w", newline="") as file:
        fieldnames = ["timestamp", "location", "pH", "humidity", "temperature", "conductivity", "nitrogen", "phosphorus", "potassium"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Data generation complete. Generated {len(rows)} rows.")

# Ensure the function runs when executed
if __name__ == "__main__":
    generate_sensor_data()
