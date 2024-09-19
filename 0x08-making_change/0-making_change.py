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
    """
    if total <= 0:
        return 0
    if total in coins:
        return 1
    coins.sort(reverse=True)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
