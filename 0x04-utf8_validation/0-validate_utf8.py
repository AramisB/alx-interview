#!/usr/bin/python3
"""
validate_utf8
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
    Only need to handle 8 leading bits of each integer
    """
    n = 0
    for num in data:
        if n == 0:
            n = _getnum(num)
        else:
            if _getnum(num) != 1:
                return False
            n -= 1
    return n == 0
