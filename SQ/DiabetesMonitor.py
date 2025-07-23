from flask import Flask, render_template
from datetime import datetime, timedelta
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Simulated patient info
    patient = {
        'name': 'John Doe',
        'age': 65
    }

    # Simulated medication schedule
    medications = [
        {'name': 'Metformin', 'time': '08:00 AM'},
        {'name': 'Insulin', 'time': '12:00 PM'},
        {'name': 'Aspirin', 'time': '06:00 PM'}
    ]

    # Simulated current glucose level
    glucose_level = 120  # You can fetch this from your DB if needed

    # Simulated glucose data for the chart
    now = datetime.now()
    timestamps = [(now - timedelta(minutes=60 * i)).strftime('%H:%M') for i in range(5)][::-1]
    levels = [random.randint(100, 130) for _ in range(5)]

    glucose_data = {
        'timestamps': timestamps,
        'levels': levels
    }

    return render_template('index.html',
                           patient=patient,
                           medications=medications,
                           glucose_level=glucose_level,
                           glucose_data=glucose_data)

if __name__ == '__main__':
    app.run(debug=True)
