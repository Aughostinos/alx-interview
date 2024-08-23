#!/usr/bin/python3
"""Task 0. Minimum Operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2

    # Loop until n is reduced to 1
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
