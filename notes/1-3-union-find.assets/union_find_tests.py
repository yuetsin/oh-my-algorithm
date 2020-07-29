#!/usr/bin/env python3

import time
from random import randint
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (function, str(t1-t0))
              )
        return result
    return function_timer


@fn_timer
def run_tests(version='naive', elem_count=10000):

    if version == 'naive':
        from union_find_naive import UnionFindSets
    elif version == 'optimized':
        from union_find_optimized import UnionFindSets
    elif version == 'tree':
        from union_find_tree import UnionFindSets
    elif version == 'weight_tree':
        from union_find_weight_tree import UnionFindSets
    else:
        from union_find_skeleton import UnionFindSets

    UFS = UnionFindSets(elem_count)

    for _ in range(elem_count):
        a, b = UFS.find(randint(0, elem_count - 1)
                        ), UFS.find(randint(0, elem_count - 1))
        ret = UFS.union(a, b)
        # print("merged sets containing element %d and %d. now they all belongs to set %d" % (a, b, ret))

    # print(UFS.payload)

    for i in range(elem_count):
        # print("element %d belongs to set %d" % (i, UFS.find(i)))
        pass
    print("done")


for version in ['naive', 'optimized', 'tree', 'weight_tree']:
    run_tests(version, 10000)
