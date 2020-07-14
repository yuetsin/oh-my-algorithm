#!/usr/bin/env python


def selection_sort(array: list):
    for i in range(len(array) - 1):
        min_value = min(array[i:])
        min_index = array.index(min_value, i)

        if min_index == i:
            # already in-place
            continue
        else:
            array[i], array[min_index] = array[min_index], array[i]
