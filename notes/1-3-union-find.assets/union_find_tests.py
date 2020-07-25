#!/usr/bin/env python3

from random import randint

version = 'naive'

if version == 'naive':
    from union_find_naive import UnionFindSets
elif version == 'basic':
    from union_find_basic import UnionFindSets
else:
    exit(-1)

elem_count = 20

UFS = UnionFindSets(elem_count)

for _ in range(elem_count):
    a, b = randint(0, elem_count - 1), randint(0, elem_count - 1)
    ret = UFS.union(a, b)
    print("merged sets containing element %d and %d. now they all belongs to set %d" % (a, b, ret))

for i in range(elem_count):
    print("element %d belongs to set %d" % (i, UFS.find(i)))
