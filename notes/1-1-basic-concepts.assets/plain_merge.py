#!/usr/bin/env python


def plain_merge(array_a: list, array_b: list) -> list:
    pointer_a, pointer_b = 0, 0
    length_a, length_b = len(array_a), len(array_b)

    result = []

    while pointer_a < length_a and pointer_b < length_b:
        if array_a[pointer_a] <= array_b[pointer_b]:
            result.append(array_a[pointer_a])
            pointer_a += 1
        else:
            result.append(array_b[pointer_b])
            pointer_b += 1

    if pointer_a != length_a:
        result += array_a[pointer_a:]
    elif pointer_b != length_b:
        result += array_b[pointer_b]

    return result
