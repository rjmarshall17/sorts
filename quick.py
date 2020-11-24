#!/usr/bin/env python3

SORTED_LIST = [8, 9, 13, 26, 29, 32, 36, 49, 58, 62, 65, 67, 69, 73, 75, 83, 85, 87, 89, 91, 92, 95, 96, 98]


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    arr_in = [96, 85, 95, 92, 62, 26, 89, 87, 29, 58, 83, 75, 13, 8, 91, 9, 98, 65, 32, 69, 36, 73, 67, 49]
    print("Unsorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    quickSort(arr_in, 0, len(arr_in) - 1)
    print("  Sorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    assert arr_in == SORTED_LIST, "The list post sort is incorrect"

# This code is contributed by Mohit Kumra
