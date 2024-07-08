import numpy as np


def bubbleSort(arr: np) -> None:
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

# Set a seed for reproducibility
np.random.seed(42)

# Generate a array of random floats between 0 and 1
arrRandomData = np.random.rand(100000)
print(arrRandomData)
print("\n")
bubbleSort(arrRandomData)
print(arrRandomData)