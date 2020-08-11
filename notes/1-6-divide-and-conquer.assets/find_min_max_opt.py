#!/usr/bin/env python

def find_min_max_opt(array: list) -> (int, int):
    if array == []:
        return None, None
    min_v = max_v = array[0]
    for v in array[1:]:
        if v < min_v:
            min_v = v
        elif v > max_v:
            max_v = v
    return min_v, max_v
