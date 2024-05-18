from flask import Flask, render_template, request
import model  # Import the model code from model.py

# Flask application setup
app = Flask(__name__)

# Route for the main webpage
@app.route('/')
def index():
  return render_template('index.html')  # Replace with your HTML template name

# Route for handling prediction requests
@app.route('/predict', methods=['POST'])
def predict():
  # Get sensor value from form submission
  sensor_value = float(request.form['sensor_value'])
  sensor_value_array = np.array([sensor_value]).reshape(1, -1)

  # Predict recommendation using the model (from model.py)
  prediction = model.model.predict(sensor_value_array)[0]

  # Get recommendation message based on prediction
  recommendation_message = {
      "Under-watering": "Water the plant immediately and thoroughly.",
      "Optimal Watering": "Maintain consistent watering practices based on plant type and environment.",
      "Over-watering": "Stop watering and allow excess water to drain. Monitor soil moisture closely."
  }[prediction]

  return render_template('result.html', prediction=prediction, recommendation_message=recommendation_message)  # Replace with your HTML template name

if __name__ == '__main__':
  app.run(debug=True)
