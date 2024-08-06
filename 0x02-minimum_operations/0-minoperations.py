#!/usr/bin/python3
"""
Minimal operations
"""
def minOperations(n):
    """
    Determine the fewest number of operations needed
    to result in exactly n H characters in a file,
    using only the operations "Copy All" and "Paste"
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
