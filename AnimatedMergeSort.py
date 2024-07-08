
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')  # or 'Qt5Agg', 'Agg', etc.
plt.ion()

def merge(arr, low, mid, high, frames):
    n1 = mid - low + 1
    n2 = high - mid

    # create temp arrays
    arr1 = [0] * n1
    arr2 = [0] * n2

    # Copy data to temp arrays arr1[] and arr2[]
    for i in range(n1):
        arr1[i] = arr[low + i]

    for j in range(n2):
        arr2[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
        frames.append(arr.copy())  # Capture the current state

    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
        frames.append(arr.copy())  # Capture the current state

    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1
        frames.append(arr.copy())  # Capture the current state

def mergeSort(arr, low, high, frames):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid, frames)
        mergeSort(arr, mid + 1, high, frames)
        merge(arr, low, mid, high, frames)

# Set a seed for reproducibility
np.random.seed(42)

# Generate an array of random floats between 0 and 100
arr = np.random.rand(100) * 100

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

# Create the animation
anim = FuncAnimation(fig, update, frames=frames, blit=True, repeat=False, interval=1)

plt.show()
plt.show(block=True)