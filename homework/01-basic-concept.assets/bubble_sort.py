#!/usr/bin/env python


def bubble_sort(array: list):
    array_len = len(array)
    swap_count = 0
    compare_count = 0

    i = 0
    is_sorted = False
    while i <= array_len - 2 and not is_sorted:
        is_sorted = True
        for j in range(array_len - 1, i, -1):
            compare_count += 1
            if array[j] < array[j - 1]:
                swap_count += 1
                array[j], array[j - 1] = array[j - 1], array[j]
                is_sorted = False
        i += 1

    print("array len: %d swap count: %d compare count: %d" %
          (array_len, swap_count, compare_count))
