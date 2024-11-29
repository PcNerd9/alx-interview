#!/usr/bin/python3

"""
Contains a single function makeChange
"""


def makeChange(coins, total):
    """
    Compute the minimum number of coins required to make up a given
    total amount, given a list of coins denominations
    """

    dp = [float("inf")] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
