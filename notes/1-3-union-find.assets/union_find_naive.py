#!/usr/bin/env python3


class UnionFindSets:

    def __init__(self, n: int):
        self.sets = {}
        for i in range(n):
            self.sets.update({i: set({i})})

    def union(self, lhs: int, rhs: int) -> int:
        lhs_set_index = self.find(lhs)
        rhs_set_index = self.find(rhs)

        if lhs_set_index is None or rhs_set_index is None:
            return None

        if lhs_set_index == rhs_set_index:
            return lhs_set_index

        lhs_set = self.sets[lhs_set_index]
        rhs_set = self.sets[rhs_set_index]

        del self.sets[lhs_set_index]
        del self.sets[rhs_set_index]

        self.sets.update({
            # always use left set name
            lhs_set_index: lhs_set.union(rhs_set)
        })

        return lhs_set_index

    def find(self, elem: int) -> int:
        for k, v in self.sets.items():
            if elem in v:
                return k

        return None
