"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""

def set_left_most_unset_bit(num):
    """
    This function sets the left most unset bit of a number.
    """
    # Find the left most unset bit
    left_most_unset_bit = num & ~(num - 1)

    # Shift the left most unset bit to the left
    left_most_unset_bit = left_most_unset_bit << 1

    # Add the left most unset bit to the original number
    num = num + left_most_unset_bit

    # Return the new number
    return num


# Test the function
assert set_left_most_unset_bit(10) == 14