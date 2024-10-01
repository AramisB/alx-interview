#!/usr/bin/python3
"""
Prime Game: Maria and Ben's optimal prime picking game.
"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of booleans representing prime numbers up to n.
    Args:
        n (int): Number to count primes up to.
    Returns:
        list: List of booleans representing prime numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False
    return sieve


def count_primes_up_to(n, sieve):
    """
    Count how many prime numbers exist up to a given number n.
    Args:
        n (int): Number to count primes up to.
        sieve (list): List of booleans representing prime numbers up to n.
    Returns:
        int: Number of primes up to n.
    """
    if n < 2:
        return 0
    return sum(sieve[:n+1])


def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.
    Returns:
        str: Name of the player ('Maria' or 'Ben').
        None: If no clear winner.
    """
    if x < 1 or not nums:
        return None

    # Step 1: Precompute primes up to the maximum number in nums
    # using Sieve of Eratosthenes
    max_num = max(nums)
    sieve = sieve_of_eratosthenes(max_num)

    # Step 2: Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Step 3: Simulate each game round
    for n in nums:
        # Count how many primes are available in the current round
        primes_count = count_primes_up_to(n, sieve)

        # If the number of primes is odd, Maria wins; if even, Ben wins
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
