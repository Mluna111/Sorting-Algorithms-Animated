import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bubbleSort(arr: np) -> None:
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                frames.append(arr.copy())  # Capture the current state


# Set a seed for reproducibility
np.random.seed(42)

# Generate an array of random floats between 0 and 100
arr = np.random.rand(50) * 100

# List to store the frames of the sorting process
frames = []

bubbleSort(arr)

# Initialize the figure and axis
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, align='edge')
ax.set_xlim(0, len(arr))
ax.set_ylim(0, 100)  # Adjust this range based on your data

# Function to update the bars in the animation
def update(frame):
    for bar, height in zip(bars, frame):
        bar.set_height(height)
    return bars

# Create the animation
anim = FuncAnimation(fig, update, frames=frames, blit=True, repeat=False, interval=1)

plt.show()
plt.show(block=True)