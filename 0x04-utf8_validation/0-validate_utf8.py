#!/usr/bin/python3
"""Module with a function that valid UTF-8"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding or false if not"""
    count = 0
    for byte in data:
        if count == 0:
            if (byte >> 5) == 0b110:
                count = 1
            elif (byte >> 4) == 0b1110:
                count = 2
            elif (byte >> 3) == 0b11110:
                count = 3
            elif (byte >> 7) == 0b1:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            count -= 1

    return count == 0
