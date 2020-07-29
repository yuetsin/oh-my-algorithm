#!/usr/bin/env python3

class UnionFindSets:
    def __init__(self, n: int):
        self.payload = [-1] * n

    def union(self, lhs: int, rhs: int) -> int:
        if lhs == rhs:
            return lhs
        
        if self.payload[lhs] < self.payload[rhs]:
            # like, -2 vs. -3
            self.payload[lhs] += self.payload[rhs]
            self.payload[rhs] = lhs
        else:
            self.payload[rhs] += self.payload[lhs]
            self.payload[lhs] = rhs
        return lhs

    def find(self, elem: int) -> int:
        while elem >= 0:
            last_elem = elem
            elem = self.payload[elem]
        return last_elem