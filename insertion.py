#!/usr/bin/env python3

SORTED_LIST = [8, 9, 13, 26, 29, 32, 36, 49, 58, 62, 65, 67, 69, 73, 75, 83, 85, 87, 89, 91, 92, 95, 96, 98]

# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == '__main__':
    # Driver code to test above
    # arr_in = [12, 11, 13, 5, 6]
    arr_in = [96, 85, 95, 92, 62, 26, 89, 87, 29, 58, 83, 75, 13, 8, 91, 9, 98, 65, 32, 69, 36, 73, 67, 49]
    print("Unsorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    insertionSort(arr_in)
    print("  Sorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    assert arr_in == SORTED_LIST, "The list post sort is incorrect"


# This code is contributed by Mohit Kumra
