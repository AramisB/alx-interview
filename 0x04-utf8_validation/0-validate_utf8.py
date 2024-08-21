#!/usr/bin/python3
"""
Combined UTF-8 validation module.
"""


def _getnum(num):
    """
    Function that returns the number of leading 1 bits
    in the most significant positions of the byte.
    """
    if (num >> 7) == 0:
        return 0  # 1-byte character (0xxxxxxx)
    n = 0
    mask = 0b10000000
    while num & mask:
        n += 1
        mask >>= 1
    return n


def validUTF8(data):
    """
    Function that determines if a given data set represents
    a valid UTF-8 encoding.
    Args: data (list): List of integers
    Returns: True if data is a valid UTF-8 encoding, else return False
    """
    n = 0
    for num in data:
        if num < 0 or num > 0x10ffff:
            return False
        if n == 0:
            n = _getnum(num)
            if n == 0:
                continue
            if n == 1 or n > 4:
                return False
        else:
            if _getnum(num) != 1:
                return False
        n -= 1
    return n == 0
