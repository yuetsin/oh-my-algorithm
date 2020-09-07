#!/usr/bin/env python3

from math import ceil
from random import shuffle
from statistics import median
array = []

rec_times = 0


# kth: counting since 0
def select(array: list, low: int, high: int, kth: int) -> int:
    print("called with len(array): %d, low: %d, high: %d" %
          (len(array), low, high))
    global rec_times
    rec_times += 1
    p = high - low + 1
    if p < 44:
        # too small? just
        return sorted(array[low: high + 1])[kth]

    q = p // 5
    groups = []

    group = []
    counter = 0
    for i in range(low, high + 1):
        group.append(array[i])
        if counter % 5 == 0:
            groups.append(group)
            group = []

        counter += 1

    midvs = [median(gp) for gp in groups]
    print("select call: to midvs")
    mm = select(midvs, 0, q - 1, ceil(q / 2))
    print("mm is", mm)
    A1, A2, A3 = [], [], []
    for item in array[low: high + 1]:
        if item < mm:
            A1.append(item)
        elif item == mm:
            A2.append(item)
        else:
            A3.append(item)

    if len(A1) >= kth:
        print("select call: len(A1) >= kth")
        return select(A1, 0, len(A1) - 1, kth)
    elif len(A1) + len(A2) > kth:
        return mm
    else:
        print("select call: len(A1) + len(A2) <= kth")
        return select(A3, 0, len(A3) - 1, kth - len(A1) - len(A2))
    # print(groups)
    # print([len(v) for v in groups])


array = list(range(105))
shuffle(array)

print("select call: parent init call")
result = select(array, 0, 104, 16)
print(result)
print("rec times: %d" % rec_times)
