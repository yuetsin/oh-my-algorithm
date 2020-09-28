#  input: two n-bit integers x and y
#         y >= 1
# output: the quotient and remainder
#         of x divided by y
def divide(x: int, y: int) -> (int, int):
    if x == 0:
        return 0, 0
    q, r = divide(x // 2, y)
    q *= 2
    r *= 2
    if x % 2:
        r += 1
    if r >= y:
        r -= y
        q += 1
    return q, r
