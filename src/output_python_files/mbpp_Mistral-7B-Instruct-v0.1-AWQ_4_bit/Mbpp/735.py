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
    # Remove the first and the last bit
    new_num = new_num >> 1
    new_num = new_num << (num_bits - 2)
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
    assert toggle_middle_bits(30) == 101
    assert toggle_middle_bits(31) == 103
    assert toggle_middle_bits(32) == 107
    assert toggle_middle_bits(33) == 109
    assert toggle_middle_bits(34) == 113
    assert toggle_middle_bits(35) == 127
    assert toggle_middle_bits(36) == 131
    assert toggle_middle_bits(37) == 137
    assert toggle_middle_bits(38) == 139
    assert toggle_middle_bits(39) == 149
    assert toggle_middle_bits(40) == 151
    assert toggle_middle_bits(41) == 157
    assert toggle_middle_bits(42) == 163
    assert toggle_middle_bits(43) == 167
    assert toggle_middle_bits(44) == 173
    assert toggle_middle_bits(45) == 179
    assert toggle_middle_bits(46) == 181
    assert toggle_middle_bits(47) == 191
    assert toggle_middle_bits(48) == 193
    assert toggle_middle_bits(49) == 197
    assert toggle_middle_bits(50) == 199
    assert toggle_middle_bits(51) == 211
    assert toggle_middle_bits(52) == 223
    assert toggle_middle_bits(53) == 227
    assert toggle_middle_bits(54) == 229
    assert toggle_middle_bits(55) == 233
    assert toggle_middle_bits(5