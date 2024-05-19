import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random


# Function to generate a random list
def random_list(y):
    return [random.randint(1, 10) / 100 for _ in range(y)]


# Function to generate a sinusoidal line with noise
def generate_sinusoidal_line_with_noise(x):
    amplitude = 1  # Adjust the amplitude of the sinusoidal wave
    frequency = 1  # Adjust the frequency of the sinusoidal wave
    phase = 0  # Adjust the phase of the sinusoidal wave
    noise = random_list(len(x))  # Generate random noise
    return amplitude * np.sin(2 * np.pi * frequency * x + phase) + noise


# Function to update the line data in each animation frame
def update(frame):
    # Clear the previous plot
    plt.clf()

    # Generate x values
    x_data = np.linspace(0, 100, 100)

    # Generate data for the sinusoidal lines with noise
    y_data1 = generate_sinusoidal_line_with_noise(x_data)
    y_data2 = generate_sinusoidal_line_with_noise(x_data)

    # Plot the sinusoidal lines
    plt.plot(x_data, y_data1, label='Sinusoidal Line 1', color='blue')
    plt.plot(x_data, y_data2, label='Sinusoidal Line 2', color='orange')

    # Fill the area between the sinusoidal lines
    plt.fill_between(x_data, y_data1, y_data2, where=(y_data1 > y_data2), interpolate=True, color='green', alpha=1)
    plt.fill_between(x_data, y_data1, y_data2, where=(y_data1 < y_data2), interpolate=True, color='red', alpha=1)

    # Set plot properties
    plt.title('Animated Sinusoidal Line Graph with Area Fill')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()


# Create a figure
fig, ax = plt.subplots()

# Create the animation
animation = FuncAnimation(fig, update, frames=range(500), interval=100)

# Show the animated plot
plt.show()
