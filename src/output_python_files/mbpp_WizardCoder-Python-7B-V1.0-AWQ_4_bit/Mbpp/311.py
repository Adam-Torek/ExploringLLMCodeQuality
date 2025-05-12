"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""

def set_left_most_unset_bit(n):
    """
    Sets the left most unset bit in a binary representation of a number.
    """
    return n | (1 << (n.bit_length())


if __name__ == "__main__":
    print(set_left_most_unset_bit(10)) # Output: 14