#!/usr/bin/env python

def find_min_max(array: list) -> (int, int):
    # x: min, y: max
    x, y = array[0], array[0]
    n = len(array)
    for i in range(1, n):
        if array[i] < x:
            x = array[i]
        # 这里实际上可以用 elif
        # 因为如果 array[i] < x 就必不可能 > y
        if array[i] > y:
            y = array[i]
    return (x, y)
