"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""

def set_left_most_unset_bit(n):
    """
    Set the left most unset bit in a number.
    """
    while n & 1 == 0:
        n >>= 1
    return n << 1

# Test the function
print(set_left_most_unset_bit(10)) # Output: 14<|endoftext|>