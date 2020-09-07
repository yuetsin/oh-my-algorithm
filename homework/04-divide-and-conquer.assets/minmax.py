#!/usr/bin/env python3

from random import shuffle

compare_count = 0


def minmax(array: list) -> (int, int):
    global compare_count
    length = len(array)
    if length == 2:
        left, right = array[0], array[1]
        compare_count += 1
        return (left, right) if left < right else (right, left)

    min1, max1 = minmax(array[:length // 2])
    min2, max2 = minmax(array[length // 2:])
    compare_count += 2
    return min(min1, min2), max(max1, max2)


for scale in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
    compare_count = 0
    example = list(range(scale))
    shuffle(example)
    minmax(example)
    print("%d, %d" %
          (len(example), compare_count))
