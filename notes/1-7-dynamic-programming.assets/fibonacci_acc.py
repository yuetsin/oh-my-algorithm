#!/usr/bin/env python

def Fibonacci(n: int) -> int:
    if n < 3:
        return 1
    f_n_1 = 1
    f_n_2 = 1
    for _ in range(3, n + 1):
        f_n = f_n_1 + f_n_2
        f_n_1, f_n_2 = f_n, f_n_1
    return f_n
