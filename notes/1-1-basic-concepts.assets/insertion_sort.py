#!/usr/bin/env python


def insertion_sort(array: list):
    for i in range(2, len(array)):
        to_insert = array[i]
        insert_point = -1
        for j in range(i - 1):
            if array[j] >= to_insert:
                # found the insert point!
                insert_point = j
                break
        if insert_point == -1:
            # to_insert value in place. no need to change anything
            continue
        else:
            del array[i]
            array.insert(insert_point, to_insert)
