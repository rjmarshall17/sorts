#!/usr/bin/env python3

SORTED_LIST = [8, 9, 13, 26, 29, 32, 36, 49, 58, 62, 65, 67, 69, 73, 75, 83, 85, 87, 89, 91, 92, 95, 96, 98]


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr_in = [96, 85, 95, 92, 62, 26, 89, 87, 29, 58, 83, 75, 13, 8, 91, 9, 98, 65, 32, 69, 36, 73, 67, 49]
    print("Unsorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    bubbleSort(arr_in)
    print("  Sorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    assert arr_in == SORTED_LIST, "The list post sort is incorrect"

