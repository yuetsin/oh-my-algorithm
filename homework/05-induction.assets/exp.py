#!/usr/bin/env python3

# return x^n
def expo(base: int, exponent: int) -> int:
    binary_exp = bin(exponent)
    result = 1
    for j in binary_exp:
        result *= result
        if j == '1':
            result *= base

    return result


def exp_sample(base: int, exponent: int) -> int:
    return pow(base, exponent)


if __name__ == '__main__':
    from random import randint
    base, exp = randint(5, 20), randint(5, 20)

    print("test   %d^%d\nexp    returns %d and\nsample returns %d" %
          (base, exp, expo(base, exp), exp_sample(base, exp)))
