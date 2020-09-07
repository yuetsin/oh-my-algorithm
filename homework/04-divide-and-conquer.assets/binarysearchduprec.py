#!/usr/bin/env python3

from random import randint

array = []
target_a, target_b = None, None


def __binarysearchrec(low: int, high: int, target: int) -> int:
    global array
    if low > high:
        return -1
    mid = (low + high) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return __binarysearchrec(low, mid - 1, target)
    else:
        return __binarysearchrec(mid + 1, high, target)


def binarysearchrecdup(low: int, high: int, no_left: bool = False, no_right: bool = False) -> (int, int):
    global array, target_a, target_b
    if low > high:
        return -1, -1

    mid = (low + high) // 2

    if no_left:
        return None, __binarysearchrec(low, high, target_b)
    elif no_right:
        return __binarysearchrec(low, high, target_a), None

    if target_b < mid:
        # target_a < target_b < mid
        return binarysearchrecdup(low, mid - 1)
    elif target_a < mid < target_b:
        # target_a < mid < target_b
        left, _ = binarysearchrecdup(low, mid - 1, False, True)
        _, right = binarysearchrecdup(mid + 1, high, True, False)
        return left, right
    else:
        # mid < target_a < target_b
        return binarysearchrecdup(mid + 1, high)


array = list(range(1024))
target_a = randint(0, 400)
target_b = randint(500, 900)
assert(target_a < target_b)
print((target_a, target_b))
print(binarysearchrecdup(0, len(array) - 1))
