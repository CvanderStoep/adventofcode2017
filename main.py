import matplotlib.pyplot as plt
import time

# Create figure and axes
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
x, y = [], []
line, = ax.plot(x, y)

for i in range(100):
    x.append(i)
    y.append(i**2)
    line.set_data(x, y)
    ax.relim()  # Rescale limits
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.1)  # Pause for a moment to update the plot

plt.ioff()  # Disable interactive mode
plt.show()
