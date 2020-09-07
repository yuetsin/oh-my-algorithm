#!/usr/bin/env python3


array = []
target = None


def binarysearchrec(low: int, high: int) -> int:
    global array, target
    if low > high:
        return -1
    mid = (low + high) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binarysearchrec(low, mid - 1)
    else:
        return binarysearchrec(mid + 1, high)


array = list(range(1024))
target = 512
print(binarysearchrec(0, len(array) - 1))
