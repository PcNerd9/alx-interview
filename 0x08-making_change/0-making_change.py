#!/usr/bin/python3

"""
Contains a single function makeChange
"""


def makeChange(coins, total):
    """
    Compute the minimum number of coins required to make up a given
    total amount, given a list of coins denominations
    """

    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
