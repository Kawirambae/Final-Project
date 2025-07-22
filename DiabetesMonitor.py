from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Home route: serves the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Check route: receives glucose readings and evaluates them
@app.route('/check', methods=['POST'])
def check_glucose():
    try:
        data = request.get_json()
        readings = data.get('readings', [])

        # Convert to floats
        readings = [float(r) for r in readings]

        if not readings:
            return jsonify({'error': 'No readings provided'}), 400

        # Simple analysis logic
        low = [r for r in readings if r < 4.0]
        high = [r for r in readings if r > 7.8]

        if low:
            return jsonify({'message': "⚠️ Warning: Some glucose levels are too low!"})
        elif high:
            return jsonify({'message': "⚠️ Warning: Some glucose levels are too high!"})
        else:
            return jsonify({'message': "✅ Glucose levels are within normal range."})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

