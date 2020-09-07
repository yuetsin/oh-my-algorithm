#!/usr/bin/env python3

from random import shuffle


def two_median(A: list, B: list) -> int:
    pass


n = 400
raw_list = list(range(2 * n))
shuffle(raw_list)

list_a = sorted(raw_list[:n])
list_b = sorted(raw_list[n:])

print("actual:      ", two_median(list_a, list_b))
print("expected:    ", n - 0.5)
