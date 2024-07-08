import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to merge two sorted halves and capture intermediate results
def merge(arr, low, mid, high, frames):
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            i += 1
        else:
            # Shift all elements between arr[i] and arr[j-1] one position to the right
            temp = arr[j]
            for k in range(j, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = temp
            i += 1
            mid += 1
            j += 1
        frames.append(arr.copy())  # Capture the current state

# Function to perform merge sort and capture intermediate results
def mergeSort(arr, low, high, frames):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid, frames)
        mergeSort(arr, mid + 1, high, frames)
        merge(arr, low, mid, high, frames)

# Set a seed for reproducibility
np.random.seed(42)

# Generate an array of random floats between 0 and 100
arr = np.random.rand(50) * 100

# List to store the frames of the sorting process
frames = []

# Perform merge sort and capture frames
mergeSort(arr, 0, len(arr) - 1, frames)

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

# Create the animation with a faster interval (20 milliseconds)
anim = FuncAnimation(fig, update, frames=frames, blit=True, repeat=False, interval=20)

# Show the plot
plt.show()

# This line will keep the plot window open until you manually close it
plt.show(block=True)
