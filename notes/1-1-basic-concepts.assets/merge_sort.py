#!/usr/bin/env python

from plain_merge import plain_merge


# simplified implementation. not considering list copy costs.
def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    split_point = len(array) // 2
    left_side, right_side = array[:split_point], array[split_point:]
    return plain_merge(merge_sort(left_side), merge_sort(right_side))
