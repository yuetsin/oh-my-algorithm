#!/usr/bin/env python


def mod_selection_sort(array: list):
    swap_count = 0
    array_len = len(array)
    for i in range(0, array_len - 1):
        for j in range(i + 1, array_len):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swap_count += 1
    print("array len: %d swap count: %d" % (array_len, swap_count))
