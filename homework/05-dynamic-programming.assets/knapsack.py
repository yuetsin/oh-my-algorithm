#!/usr/bin/env python3
from prettytable import PrettyTable


class Good:
    def __init__(self, wv: tuple):
        self.weight = wv[0]
        self.value = wv[1]


goods = [Good(g) for g in [(2, 3), (3, 4), (5, 5), (6, 7)]]

good_count = len(goods)
knapsack_capacity = 11

dp = [[None] * (knapsack_capacity + 1) for _ in range(good_count)]


def solve_knapsack(good_index, available_capacity):
    global dp

    if dp[good_index][available_capacity] != None:
        return dp[good_index][available_capacity]

    if good_index == 0 or available_capacity == 0:
        dp[good_index][available_capacity] = (0, [])
        return (0, [])

    weight, value = goods[good_index].weight, goods[good_index].value
    if weight > available_capacity:
        # this good can't be put into knapsack anyway
        res = solve_knapsack(good_index - 1, available_capacity)
        dp[good_index][available_capacity] = res
        return res
    else:
        not_put, no_comb = solve_knapsack(good_index - 1, available_capacity)
        do_put, do_comb = solve_knapsack(
            good_index - 1, available_capacity - weight)
        do_put += value
        do_comb += [good_index]
        if not_put > do_put:
            dp[good_index][available_capacity] = not_put, no_comb
            return not_put, no_comb
        else:
            dp[good_index][available_capacity] = do_put, do_comb
            return do_put, do_comb


max_val = solve_knapsack(good_count - 1, knapsack_capacity)


t = PrettyTable(['C%d' % i for i in range(knapsack_capacity + 1)])
for line in dp:
    t.add_row(line)
print(t)
