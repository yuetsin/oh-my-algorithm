#!/usr/bin/env python3

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
    if m == array_len - 1:
        print(array)
    else:
        for j in range(m, array_len):
            array[j], array[m] = array[m], array[j]
            perm_helper(m + 1)
            array[j], array[m] = array[m], array[j]


if __name__ == '__main__':
    generate_perm(4)
