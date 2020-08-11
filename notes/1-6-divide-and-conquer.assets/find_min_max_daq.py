#!/usr/bin/env python

def find_min_max_dvq(array: list) -> (int, int):
    def __minmax(low: int, high: int) -> (int, int):
        if high - low == 1:
            low_v, high_v = array[low], array[high]
            return (low_v, high_v) if low_v < high_v else (high_v, low_v)
        else:
            mid = (low + high) // 2
            x1, y1 = __minmax(low, mid)
            x2, y2 = __minmax(mid + 1, high)
            return min(x1, x2), max(y1, y2)
    if array == []:
        return None, None
    return __minmax(0, len(array) - 1)
