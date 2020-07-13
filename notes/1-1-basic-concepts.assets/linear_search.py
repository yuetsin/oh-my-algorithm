#!/usr/bin/env python


def linear_search(array: list, target) -> int:
    index = 0
    length = len(array)
    while index < length:
        if array[index] == target:
            return index
        index += 1
    return -1
