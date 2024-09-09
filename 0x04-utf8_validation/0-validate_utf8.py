#!/usr/bin/python3
"""
Definesa UTF-8 validation function
"""


def validUTF8(data):
    """
    UTF-8 Validation function
    """
    n_bytes = 0

    byte1_mask = 0b10000000
    byte2_mask = 0b11000000
    byte3_mask = 0b11100000
    byte4_mask = 0b11110000
    cont_mask = 0b11000000

    for byte in data:
        byte = byte & 0xFF

        if n_bytes == 0:
            if byte & byte1_mask == 0:
                # 1-byte character, ASCII range (0xxxxxxx)
                continue
            elif byte & byte3_mask == byte2_mask:
                # 2-byte character (110xxxxx)
                n_bytes = 1  # Expect 1 continuation byte
            elif byte & byte4_mask == byte3_mask:
                # 3-byte character (1110xxxx)
                n_bytes = 2  # Expect 2 continuation bytes
            elif byte & cont_mask == byte4_mask:
                # 4-byte character (11110xxx)
                n_bytes = 3  # Expect 3 continuation bytes
            else:
                # Invalid first byte
                return False
        else:
            # If we are expecting continuation bytes
            if byte & cont_mask != byte1_mask:
                return False
            n_bytes -= 1  # One less continuation byte to expect

    return n_bytes == 0
