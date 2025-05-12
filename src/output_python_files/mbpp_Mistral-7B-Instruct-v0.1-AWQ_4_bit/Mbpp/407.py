"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""

def rearrange_bigger(num):
    """
    This function takes a number as input and returns the next bigger number by rearranging its digits.
    """
    # First we convert the number to a string so that we can easily sort its digits
    num_str = str(num)
    # Then we sort the digits in descending order
    num_str = sorted(num_str, reverse=True)
    # Finally we convert the sorted string back to a number and return it
    return int(num_str)


if __name__ == "__main__":
    assert rearrange_bigger(12) == 21
    assert rearrange_bigger(15) == 51
    assert rearrange_bigger(10) == 10
    assert rearrange_bigger(13) == 31
    assert rearrange_bigger(14) == 41