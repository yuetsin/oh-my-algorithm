#!/usr/bin/env python3

def __two_sum(array: list, since: int, till: int, target: int) -> bool:
    if since >= till:
        return False

    current_sum = array[s] + array[t]
    if current_sum == target:
        return True
    elif current_sum > target:
        return __two_sum(array, since, till - 1, target)
    else:
        return __two_sum(array, since + 1, till, target)


def two_sum(array: list, target: int) -> bool:
    return __two_sum(array, 1, len(array), target)
