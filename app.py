from flask import Flask, render_template

app = Flask(__name__)

# Simulated data for injection points
injection_data = [
    {"label": "P1", "pH": 6.5, "humidity": 45, "temperature": 22.5, "conductivity": 300, "nitrogen": 10, "phosphorus": 15, "potassium": 20},
    {"label": "P2", "pH": 6.6, "humidity": 46, "temperature": 22.7, "conductivity": 310, "nitrogen": 11, "phosphorus": 14, "potassium": 19},
    {"label": "P3", "pH": 6.7, "humidity": 47, "temperature": 22.9, "conductivity": 320, "nitrogen": 12, "phosphorus": 13, "potassium": 18},
    {"label": "P4", "pH": 6.8, "humidity": 48, "temperature": 23.1, "conductivity": 330, "nitrogen": 13, "phosphorus": 12, "potassium": 17},
    {"label": "P5", "pH": 6.9, "humidity": 49, "temperature": 23.3, "conductivity": 340, "nitrogen": 14, "phosphorus": 11, "potassium": 16},
    {"label": "P6", "pH": 7.0, "humidity": 50, "temperature": 23.5, "conductivity": 350, "nitrogen": 15, "phosphorus": 10, "potassium": 15},
    {"label": "P7", "pH": 7.1, "humidity": 51, "temperature": 23.7, "conductivity": 360, "nitrogen": 16, "phosphorus": 9, "potassium": 14},
    {"label": "P8", "pH": 7.2, "humidity": 52, "temperature": 23.9, "conductivity": 370, "nitrogen": 17, "phosphorus": 8, "potassium": 13},
    {"label": "P9", "pH": 7.3, "humidity": 53, "temperature": 24.1, "conductivity": 380, "nitrogen": 18, "phosphorus": 7, "potassium": 12},
    {"label": "P10", "pH": 7.4, "humidity": 54, "temperature": 24.3, "conductivity": 390, "nitrogen": 19, "phosphorus": 6, "potassium": 11},
]

@app.route('/')
def home():
    return render_template('index.html', injection_points=injection_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

