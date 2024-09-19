Coin Change Problem
Description
The Coin Change Problem is a classic algorithmic problem that involves finding the fewest number of coins needed to make a specific amount of money using a given set of coin denominations. This problem can be solved using different strategies, such as a greedy algorithm or dynamic programming.

Problem Statement
Given an integer amount and a list of integers representing different coin denominations coins[], your task is to determine the minimum number of coins required to make up the amount. If the amount cannot be made up with the given coins, return -1.

Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
Explanation: It's not possible to make 3 with only coin denomination 2.


Approaches
1. Greedy Algorithm
A greedy algorithm tries to solve the problem by choosing the largest denomination at every step. While this can work for certain sets of coin denominations (like [1, 5, 10, 25]), it doesn’t guarantee an optimal solution for arbitrary coin sets. In cases where the greedy approach fails, it may use more coins than necessary.

2. Dynamic Programming
Dynamic programming is a more reliable method for solving the coin change problem, especially when coin denominations are irregular. It builds the solution bottom-up by solving smaller subproblems (e.g., the minimum number of coins for amounts smaller than the target) and using those to construct the final solution.

Principles:
Optimal Substructure: The solution to a larger problem can be built from optimal solutions to subproblems.
Overlapping Subproblems: The problem can be broken down into smaller subproblems that are reused multiple times.
In this approach, we maintain a table dp[], where dp[i] represents the minimum number of coins required to make i amount. The final answer will be stored in dp[amount].

Algorithmic Complexity
Greedy Algorithm:
Time Complexity: O(n) for n coin denominations, but it might not always provide the correct solution.
Space Complexity: O(1).

Dynamic Programming:
Time Complexity: O(n * amount), where n is the number of denominations.
Space Complexity: O(amount) for the dp array used to store intermediate solutions.

Python Code Implementation
Here’s a Python implementation of the dynamic programming approach:
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

Example Usage
coins = [1, 2, 5]
amount = 11
result = coinChange(coins, amount)
print(f"Minimum coins required: {result}")  # Output: 3
