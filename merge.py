#!/usr/bin/env python3

SORTED_LIST = [8, 9, 13, 26, 29, 32, 36, 49, 58, 62, 65, 67, 69, 73, 75, 83, 85, 87, 89, 91, 92, 95, 96, 98]


def mergeSort(arr):
    # print("Splitting ", arr)
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    # print("Merging ",arr)


if __name__ == '__main__':
    arr_in = [96, 85, 95, 92, 62, 26, 89, 87, 29, 58, 83, 75, 13, 8, 91, 9, 98, 65, 32, 69, 36, 73, 67, 49]
    print("Unsorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    mergeSort(arr_in)
    print("  Sorted list: %s" % [arr_in[i] for i in range(len(arr_in))])
    assert arr_in == SORTED_LIST, "The list post sort is incorrect"
