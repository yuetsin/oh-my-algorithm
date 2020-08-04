#!/usr/bin/env python3
array = []
array_len = -1


def generate_perm(n):
    global array
    global array_len
    array = [0] * n
    array_len = n
    perm_helper(n)


def perm_helper(m: int):
    global array
    global array_len
    if m == 0:
        print(array)
    else:
        for j in range(array_len):
            if array[j] == 0:
                array[j] = m
                perm_helper(m - 1)
                array[j] = 0


if __name__ == '__main__':
    generate_perm(4)
