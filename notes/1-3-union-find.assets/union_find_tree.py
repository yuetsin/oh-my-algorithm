#!/usr/bin/env python3

class UnionFindSets:
    def __init__(self, n: int):
        self.payload = [-1] * n

    def union(self, lhs: int, rhs: int) -> int:
        if lhs == rhs:
            return lhs
        
        self.payload[lhs] += self.payload[rhs]
        self.payload[rhs] = lhs
        return lhs

    def find(self, elem: int) -> int:
        while elem >= 0:
            last_elem = elem
            elem = self.payload[elem]
        return last_elem