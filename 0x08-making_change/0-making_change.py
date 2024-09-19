#!/usr/bin/python3
"""
This module contains the makeChange function
for the coin change problem
"""


def makeChange(coins, total):
    """
    This function determines the fewest number of coins
    needed to meet a given amount total.
    Args: coins - list of the value of the coins for the change
          total - total amount of coins
    Returns: fewest number of coins needed
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    Using greedy algorithm
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total == 0:
        return count
    return -1
