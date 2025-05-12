"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(num):
    """
    Function to set all even bits of a given number
    :param num: integer number
    :return: integer number with all even bits set
    """
    mask = 0xAAABBBCCCCDDDDEEEEFFFF0000
    return num | mask

# Test the function
assert even_bit_set_number(10) == 14
assert even_bit_set_number(15) == 22
assert even_bit_set_number(0) == 0
assert even_bit_set_number(1) == 1
assert even_bit_set_number(128) == 128
assert even_bit_set_number(129) == 130
assert even_bit_set_number(130) == 132
assert even_bit_set_number(131) == 131
assert even_bit_set_number(132) == 134
assert even_bit_set_number(133) == 134
assert even_bit_set_number(134) == 136
assert even_bit_set_number(135) == 136
assert even_bit_set_number(136) == 136
assert even_bit_set_number(137) == 138
assert even_bit_set_number(138) == 140
assert even_bit_set_number(139) == 140
assert even_bit_set_number(140) == 142
assert even_bit_set_number(141) == 142
assert even_bit_set_number(142) == 142
assert even_bit_set_number(143) == 146
assert even_bit_set_number(144) == 144
assert even_bit_set_number(145) == 148
assert even_bit_set_number(146) == 148
assert even_bit_set_number(147) == 148
assert even_bit_set_number(148) == 150
assert even_bit_set_number(149) == 150
assert even_bit_set_number(150) == 150
assert even_bit_set_number(151) == 152
assert even_bit_set_number(152) == 154
assert even_bit_set_number(153) == 154
assert even_bit_set_number(154) == 154
assert even_bit_set_number(155) == 156
assert even_bit_set_number(156) == 156
assert even_bit_set_number(157) == 156
assert even_bit_set_number(158) == 160
assert even_bit_set_number(159) == 160
assert even_bit_set_number(160) == 160
assert even_bit_set_number(161) == 162
assert even_bit_set_number(162) == 164
assert even_bit_set_number(163) == 164
assert even_bit_set_number(164) == 164
assert even_bit_set_number(165) == 166
assert even_bit_set_number(166) == 166
assert even_bit_set_number(167) == 166
assert even_bit_set_number(168)