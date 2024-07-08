#MergeSort
import numpy as np

def merge(arr: np, low: int, mid: int, high: int):
    n1 = mid - low + 1
    n2 = high - mid

    # create temp arrays
    arr1 = [0] * (n1)
    arr2 = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        arr1[i] = arr[low + i]

    for j in range(0, n2):
        arr2[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = low
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr[k] = arr2[j]
            j += 1
            k += 1


    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1


def mergeSort(arr: np, low: int, high: int) -> None:
    if high <= low:
        return
    mid = (low + high-1) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)

# Set a seed for reproducibility
np.random.seed(42)

# Generate a array of random floats between 0 and 1
arrRandomData = np.random.rand(100000)
print(arrRandomData)
print("\n")
mergeSort(arrRandomData, 0, arrRandomData.size-1)
print(arrRandomData)




