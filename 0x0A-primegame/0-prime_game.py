#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game played between Maria and Ben.

    Parameters:
    x (int): The number of rounds.
    nums (list of int): List containing the upper bound n for each round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
         If the result is a tie, return None.
    """
    if x < 1 or not nums:
        return None

    def sieve(n):
        """
        Generate a list of boolean values
        indicating prime status for numbers 0 to n.

        Parameters:
        n (int): The upper bound to generate primes for.

        Returns:
            list of bool: List where index i is
            True if i is a prime number, otherwise False.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p] is True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
        return is_prime

    max_n = max(nums)
    primes = sieve(max_n)

    def count_primes(n):
        """
        Count the number of prime numbers up to n.

        Parameters:
        n (int): The upper bound to count primes for.

        Returns:
        int: The count of prime numbers up to n.
        """
        count = 0
        for i in range(1, n + 1):
            if primes[i]:
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_left = count_primes(n)
        if primes_left % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
