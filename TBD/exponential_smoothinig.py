import matplotlib.pyplot as plt
import numpy as np

# Generate a synthetic dataset with a gradually increasing trend
np.random.seed(42)
time = np.arange(100)
Y = 10 + time * 0.1 + np.random.normal(0, 1, 100)  # Increasing trend with some noise

# Smoothing constant
alpha = 0.3

# Initial smoothed value
S = [Y[0]]

# Compute smoothed values
for t in range(1, len(Y)):
    S_t = alpha * Y[t] + (1 - alpha) * S[t-1]
    S.append(S_t)

# Plotting the actual data points as a scatter plot
plt.scatter(range(1, len(Y) + 1), Y, color='blue', label='Actual Data (Y_t)', s=10)

# Plotting the smoothed data points as a scatter plot
plt.scatter(range(1, len(S) + 1), S, color='red', label='Smoothed Data (S_t)', s=10)

# Adding titles and labels
plt.title('Simple Exponential Smoothing on Gradually Increasing Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
