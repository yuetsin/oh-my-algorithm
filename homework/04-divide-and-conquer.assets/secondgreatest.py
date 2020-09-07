#!/usr/bin/env python3

from random import shuffle


def secondgreatest(array: list) -> int:
    greatest = None
    second_greatest = None

    for num in array:
        if greatest == None:
            greatest = num
        elif num > greatest:
            # resign
            second_greatest = greatest
            greatest = num
        elif second_greatest == None:
            second_greatest = num
        elif num > second_greatest:
            second_greatest = num

    return second_greatest


array = list(range(4096))
shuffle(array)
print(secondgreatest(array))
