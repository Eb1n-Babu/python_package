import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Load and prepare data
df = pd.read_csv("data.csv")
features = df[['Weight', 'Volume']]
target = df['CO2']

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Train model
model = LinearRegression()
model.fit(scaled_features, target)

# Predict: use consistent units (e.g., Volume in cm³)
# If you meant 1.3 liters, convert to cm³: 1.3 * 1000 = 1300
new_input = pd.DataFrame([[2300, 1300]], columns=['Weight', 'Volume'])
scaled_input = scaler.transform(new_input)

# Predict CO2
predicted_CO2 = model.predict(scaled_input)
print(f"Predicted CO2 emission: {predicted_CO2[0]:.2f} g/km")