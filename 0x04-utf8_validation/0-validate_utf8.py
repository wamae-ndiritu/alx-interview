#!/usr/bin/env python3
"""
UTF8 Validation
"""


def validUTF8(data):
    """
    Handles utf8-validation
    """
    num_bytes_to_follow = 0

    for byte in data:
        byte = byte & 0xFF  # Ensure only 8 bits are considered
        if num_bytes_to_follow == 0:
            if byte >> 7 == 0b0:
                continue  # 1-byte character
            elif byte >> 5 == 0b110:
                num_bytes_to_follow = 1  # 2-byte character
            elif byte >> 4 == 0b1110:
                num_bytes_to_follow = 2  # 3-byte character
            elif byte >> 3 == 0b11110:
                num_bytes_to_follow = 3  # 4-byte character
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False  # Invalid following byte
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
