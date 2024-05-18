import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Define watering recommendation function based on sensor value
def get_watering_recommendation(sensor_value):
  if sensor_value < 350:
    return "Under-watering"
  elif sensor_value > 850:
    return "Over-watering"
  else:
    return "Optimal Watering"

# Load data from CSV file (replace 'moisture.csv' with your actual path)
data = pd.read_csv('moisture.csv')

# Create empty list for recommendations (if 'Recommendation' column doesn't exist)
if 'Recommendation' not in data.columns:
  recommendations = []
  for sensor_value in data['SensorValue']:
    recommendation = get_watering_recommendation(sensor_value)
    recommendations.append(recommendation)
  data['Recommendation'] = recommendations

# Define sensor values and target variable (watering recommendation)
sensor_values = data['SensorValue']
target_variable = data['Recommendation']

# Split data into training and testing sets (optional, for model retraining)
X_train, X_test, y_train, y_test = train_test_split(sensor_values.values.reshape(-1, 1), target_variable, test_size=0.2)

# Create and train the Decision Tree Classifier model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)  # Train the model (or load a pre-trained model if desired)
