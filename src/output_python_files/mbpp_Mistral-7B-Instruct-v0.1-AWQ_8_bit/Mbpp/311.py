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

    # Set the left most unset bit
    num = num | left_most_unset_bit

    # Return the number
    return num


if __name__ == "__main__":
    assert set_left_most_unset_bit(10) == 14