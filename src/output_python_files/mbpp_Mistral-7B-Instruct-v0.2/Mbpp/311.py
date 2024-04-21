"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
def set_left_most_unset_bit(num):
    """
    Function to set the left most unset bit in a given number.
    :param num: An integer number
    :return: The number with the left most unset bit set
    """
    return num | (1 << (len(bin(num)) - len(bin(num)[::-1].find('0'))))

assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(5) == 6
assert set_left_most_unset_bit(1) == 2
assert set_left_most_unset_bit(0) == 1
assert set_left_most_unset_bit(15) == 16
assert set_left_most_unset_bit(128) == 129
assert set_left_most_unset_bit(127) == 128
assert set_left_most_unset_bit(126) == 127
assert set_left_most_unset_bit(125) == 126
assert set_left_most_unset_bit(124) == 125
assert set_left_most_unset_bit(123) == 124
assert set_left_most_unset_bit(122) == 123
assert set_left_most_unset_bit(121) == 122
assert set_left_most_unset_bit(120) == 121
assert set_left_most_unset_bit(119) == 120
assert set_left_most_unset_bit(118) == 119
assert set_left_most_unset_bit(117) == 118
assert set_left_most_unset_bit(116) == 117
assert set_left_most_unset_bit(115) == 116
assert set_left_most_unset_bit(114) == 115
assert set_left_most_unset_bit(113) == 114
assert set_left_most_unset_bit(112) == 113
assert set_left_most_unset_bit(111) == 112
assert set_left_most_unset_bit(110) == 111
assert set_left_most_unset_bit(109) == 110
assert set_left_most_unset_bit(108) == 109
assert set_left_most_unset_bit(107) == 108
assert set_left_most_unset_bit(106) == 107
assert set_left_most_unset_bit(105) == 106
assert set_left_most_unset_bit(104) == 105
assert set_left_most_unset_bit(103) == 104
assert set_left_most_unset_bit(102) == 103
assert set_left_most_unset_bit(101) == 102
assert set_left_most_unset_bit(100) == 101
assert set_left_most_unset_bit(99) == 100
assert set_left_most_unset_bit(98) == 99
assert set_left_most_unset_bit(97) == 98
assert set_left_most_unset_bit(96) == 97
assert set_left_most_unset_bit(95) == 96
assert set_left_most_unset_bit(94) == 95
assert set_left_most_unset_bit(93) == 94
assert set_left_most_unset_bit(92) == 93
assert set