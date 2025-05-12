"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""

def set_left_most_unset_bit(n):
    return n | (1 << (n.bit_length())

print(set_left_most_unset_bit(10)) # Output: 14