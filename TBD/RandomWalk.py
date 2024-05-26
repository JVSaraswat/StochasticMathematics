import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_steps = 1000000  # Number of steps in the random walk
num_walks = 10  # Number of random walk paths to simulate

# Simulate random walks
walks = np.cumsum(np.random.choice([-1, 1], size=(num_walks, num_steps)), axis=1)

# Calculate the sqrt(t) bounds
time_steps = np.arange(num_steps)
sqrt_bounds = np.sqrt(time_steps)

# Plotting
plt.figure(figsize=(12, 6))
for i in range(num_walks):
    plt.plot(walks[i], alpha=0.7)

# Plot the sqrt(t) bounds
plt.plot(time_steps, sqrt_bounds, 'r--', label='$\sqrt{t}$')
plt.plot(time_steps, -sqrt_bounds, 'r--')

# Labels and title
plt.title('Simple Symmetric Random Walks')
plt.xlabel('Steps')
plt.ylabel('Position')
plt.legend(['Random Walks', '$\pm\sqrt{t}$ bounds'])
plt.grid(True)
plt.show()

# Calculate the proportion of steps within the bounds for each walk
within_bounds_proportions = []

for walk in walks:
    within_bounds = np.abs(walk) <= sqrt_bounds
    proportion_within_bounds = np.mean(within_bounds)
    within_bounds_proportions.append(proportion_within_bounds)
"""
# Plotting the results
plt.figure(figsize=(10, 6))
plt.bar(range(num_walks), within_bounds_proportions)
plt.xlabel('Random Walk Index')
plt.ylabel('Proportion of Steps within $\pm\sqrt{t}$ Bounds')
plt.title('Proportion of Steps within $\pm\sqrt{t}$ Bounds for Each Random Walk')
plt.ylim(0, 1)
plt.grid(True)
plt.show()
"""
# Print the results along with avg proportion
avg = 0
for i, proportion in enumerate(within_bounds_proportions):
    print(f'Random Walk {i + 1}: {proportion * 100:.2f}% of steps within bounds')
    avg = avg + proportion

print("Total steps within bounds: "+str((avg * 100) / num_walks))
