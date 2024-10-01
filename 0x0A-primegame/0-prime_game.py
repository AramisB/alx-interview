#!/usr/bin/python3
"""
Module for a prime game
"""


def sieve_of_eratosthenes(n):
    """
    Helper function that returns a list of prime numbers up to n
    using the Sieve of Eratosthenes algorithm.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def isWinner(x, nums):
    """
    Determine the winner of the prime game
    Args: x (int): number of rounds
          nums (list): list of numbers
    Returns: str: name of the winner, Ben or Maria
             None if the winner cannot be determined
    """
    if x < 1 or not nums:
        return None
    # track number of wins
    ben_wins = 0
    maria_wins = 0

    max_num = max(nums)

    # create list of primes up to max_num
    prime_list = sieve_of_eratosthenes(max_num)

    for num in nums:
        # copy the current set of numbers for the game round
        game_set = list(range(1, num + 1))
        # maria starts first
        current_player = "Maria"
        # track available numbers
        while True:
            available_primes = [prime for prime in prime_list
                                if prime in game_set]
            if not available_primes:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            # remove the first available prime
            # and its multiples in the game_set
            prime = available_primes[0]
            game_set = [num for num in game_set if num % prime != 0]
            # switch players for the next game
            current_player = "Ben" if current_player == "Maria" else "Maria"

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
