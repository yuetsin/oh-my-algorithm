#!/usr/bin/env python3


class UnionFindSets:
    def __init__(self, n: int):
        self.payload = list(range(n))

    def union(self, lhs: int, rhs: int) -> int:
        for key, value in enumerate(self.payload):
            if value == rhs:
                self.payload[key] = self.payload[lhs]
        return self.payload[lhs]

    def find(self, elem: int) -> int:
        return self.payload[elem]