"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
def set_left_most_unset_bit(num):
    """
    This function sets the left most unset bit in the given number.
    :param num: An integer number
    :return: An integer number with the left most unset bit set
    """
    # Find the position of the left most unset bit using bitwise AND with (num-1)
    left_most_unset_bit_position = num & ~(num - 1)

    # Set the left most unset bit using bitwise OR with 1
    return num | left_most_unset_bit_position

# Test the function
assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(5) == 7
assert set_left_most_unset_bit(1) == 3
assert set_left_most_unset_bit(0) == 1
assert set_left_most_unset_bit(-1) == 0
assert set_left_most_unset_bit(128) == 129
assert set_left_most_unset_bit(127) == 128
assert set_left_most_unset_bit(126) == 128
assert set_left_most_unset_bit(125) == 127
assert set_left_most_unset_bit(124) == 127
assert set_left_most_unset_bit(123) == 127
assert set_left_most_unset_bit(122) == 127
assert set_left_most_unset_bit(121) == 127
assert set_left_most_unset_bit(120) == 127
assert set_left_most_unset_bit(119) == 127
assert set_left_most_unset_bit(118) == 127
assert set_left_most_unset_bit(117) == 127
assert set_left_most_unset_bit(116) == 127
assert set_left_most_unset_bit(115) == 127
assert set_left_most_unset_bit(114) == 127
assert set_left_most_unset_bit(113) == 127
assert set_left_most_unset_bit(112) == 127
assert set_left_most_unset_bit(111) == 127
assert set_left_most_unset_bit(110) == 127
assert set_left_most_unset_bit(109) == 127
assert set_left_most_unset_bit(108) == 127
assert set_left_most_unset_bit(107) == 127
assert set_left_most_unset_bit(106) == 127
assert set_left_most_unset_bit(105) == 127
assert set_left_most_unset_bit(104) == 127
assert set_left_most_unset_bit(103) == 127
assert set_left_most_unset_bit(102) == 127
assert set_left_most_unset_bit(101) == 127
assert set_left_most_unset_bit(100) == 127
assert set_left_most_unset_bit(99) == 127
assert set_left_most_unset_bit(98) == 127
assert set_left_most_unset_bit(97) == 127
assert set_