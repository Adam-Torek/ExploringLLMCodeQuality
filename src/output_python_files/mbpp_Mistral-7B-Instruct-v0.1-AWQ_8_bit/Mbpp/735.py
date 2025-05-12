"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""

def toggle_middle_bits(num):
    """
    Toggle all bits except the first and the last bit.
    :param num: int
    :return: int
    """
    # Get the number of bits in the number
    num_bits = len(str(num))
    # Create a new number with all bits set to 1
    new_num = (1 << num_bits) - 1
    # Toggle all bits except the first and the last bit
    new_num ^= num
    # Return the new number
    return new_num


if __name__ == '__main__':
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 21
    assert toggle_middle_bits(11) == 23
    assert toggle_middle_bits(12) == 27
    assert toggle_middle_bits(13) == 31
    assert toggle_middle_bits(14) == 33
    assert toggle_middle_bits(15) == 37
    assert toggle_middle_bits(16) == 41
    assert toggle_middle_bits(17) == 43
    assert toggle_middle_bits(18) == 47
    assert toggle_middle_bits(19) == 51
    assert toggle_middle_bits(20) == 53
    assert toggle_middle_bits(21) == 59
    assert toggle_middle_bits(22) == 61
    assert toggle_middle_bits(23) == 67
    assert toggle_middle_bits(24) == 71
    assert toggle_middle_bits(25) == 73
    assert toggle_middle_bits(26) == 79
    assert toggle_middle_bits(27) == 83
    assert toggle_middle_bits(28) == 89
    assert toggle_middle_bits(29) == 97
    assert toggle_middle_bits(30) == 103
    assert toggle_middle_bits(31) == 107
    assert toggle_middle_bits(32) == 113
    assert toggle_middle_bits(33) == 127
    assert toggle_middle_bits(34) == 131
    assert toggle_middle_bits(35) == 137
    assert toggle_middle_bits(36) == 139
    assert toggle_middle_bits(37) == 149
    assert toggle_middle_bits(38) == 151
    assert toggle_middle_bits(39) == 157
    assert toggle_middle_bits(40) == 163
    assert toggle_middle_bits(41) == 167
    assert toggle_middle_bits(42) == 173
    assert toggle_middle_bits(43) == 179
    assert toggle_middle_bits(44) == 181
    assert toggle_middle_bits(45) == 191
    assert toggle_middle_bits(46) == 193
    assert toggle_middle_bits(47) == 197
    assert toggle_middle_bits(48) == 199
    assert toggle_middle_bits(49) == 211
    assert toggle_middle_bits(50) == 223
    assert toggle_middle_bits(51) == 227
    assert toggle_middle_bits(52) == 229
    assert toggle_middle_bits(53) == 233
    assert toggle_middle_bits(54) == 239
    assert toggle_middle_bits(55) == 241
    assert toggle_middle_bits(56) == 251
    assert toggle_middle_bits(57) == 257
    assert toggle_