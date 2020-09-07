#!/usr/bin/env python3

from random import shuffle


array = []
array_len = -1


def generate_perm(n):
    global array
    global array_len
    array = list(range(1, n + 1))
    array_len = n
    perm_helper(0)


def perm_helper(m: int):
    global array
    global array_len
    global arrays
    if m == array_len - 1:
        arrays.append(tuple(array))
    else:
        for j in range(m, array_len):
            array[j], array[m] = array[m], array[j]
            perm_helper(m + 1)
            array[j], array[m] = array[m], array[j]


array = []


def split(low: int, high: int):
    global array, swap_count
    i = low
    # choose the first element as separator
    x = array[low]

    for j in range(low + 1, high + 1):
        if array[j] <= x:
            i += 1
            if i != j:
                swap_count += 1
                array[i], array[j] = array[j], array[i]

    swap_count += 1
    array[low], array[i] = array[i], array[low]


N = int(input("N = ? >>> "))

arrays = []

generate_perm(N)

max_swap = 0
worst_case = []

for array_tuple in arrays:
    swap_count = 0
    array = list(array_tuple)

    # print("before: ", array)
    # print("SPLIT with ", array[0])
    split(0, len(array) - 1)
    # print("after: ", array)
    # print("swap count: ", swap_count)

    if swap_count > max_swap:
        worst_case = [array_tuple]
        max_swap = swap_count
    elif swap_count == max_swap:
        worst_case.append(array_tuple)

print("when N = %d, max_swap (-1) = %d" % (N, max_swap - 1))
print("worst case: ", worst_case)
