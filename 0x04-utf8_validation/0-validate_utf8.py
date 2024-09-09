def validUTF8(data):
    n_bytes = 0  # Number of continuation bytes we expect
    
    # Masks for determining how many bytes a character occupies
    byte1_mask = 0b10000000  # Mask for 1-byte characters (0xxxxxxx)
    byte2_mask = 0b11000000  # Mask for leading byte of 2-byte characters (110xxxxx)
    byte3_mask = 0b11100000  # Mask for leading byte of 3-byte characters (1110xxxx)
    byte4_mask = 0b11110000  # Mask for leading byte of 4-byte characters (11110xxx)
    cont_mask = 0b11000000   # Mask for continuation bytes (10xxxxxx)
    
    for byte in data:
        byte = byte & 0xFF  # Only consider the last 8 bits of the integer (as 1 byte)
        
        if n_bytes == 0:  # If we are not expecting any continuation bytes
            # Determine how many bytes the character should take up based on the first byte
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
                # If the byte doesn't match the continuation byte pattern (10xxxxxx), it's invalid
                return False
            n_bytes -= 1  # One less continuation byte to expect
    
    # If we finish and still expect more continuation bytes, the input is invalid
    return n_bytes == 0

