import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# 1. Load data
df = pd.read_csv('ETH-USD.csv')
data = df['Close'].values.reshape(-1, 1)

# 2. Scale data (Required for RNN stability)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# 3. Create sequences (30-day window)
window_size = 30
X, y = [], []
for i in range(window_size, len(scaled_data)):
    X.append(scaled_data[i-window_size:i, 0])
    y.append(scaled_data[i, 0])
X, y = np.array(X), np.array(y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# 4. Build a Plain RNN Model
# This uses the standard SimpleRNN layer
model = Sequential([
    SimpleRNN(units=32, input_shape=(X.shape[1], 1), activation='tanh'),
    Dense(units=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# 5. Train the model
model.fit(X, y, epochs=10, batch_size=32, verbose=0)

# 6. Generate Predictions for the plot
predictions = model.predict(X)
predictions = scaler.inverse_transform(predictions)

# 7. Presentation-ready Plotting
plt.figure(figsize=(12, 6))
actual_data = data[window_size:]
dates = pd.to_datetime(df['Date']).iloc[window_size:]

plt.plot(dates, actual_data, color='blue', label='Actual Price', linewidth=1.5)
plt.plot(dates, predictions, color='orange', label='Plain RNN Prediction', linestyle='--')
plt.title('Ethereum Price: Plain RNN Trend Analysis', fontsize=14)
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()