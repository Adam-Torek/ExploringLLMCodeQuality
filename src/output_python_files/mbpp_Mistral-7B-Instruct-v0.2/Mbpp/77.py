"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_divisible_by_eleven(num):
    """
    This function checks whether a number is divisible by 11 or not.
    :param num: an integer number
    :return: True if the number is divisible by 11, False otherwise
    """
    # Calculate the sum of digits in the number
    sum_digits = sum(int(digit) for digit in str(num))

    # Check if the sum of digits is divisible by 11
    return sum_digits % 11 == 0

# Test the function
assert is_divisible_by_eleven(12345) == False
assert is_divisible_by_eleven(1234567890) == True
assert is_divisible_by_eleven(1234555555) == True
assert is_divisible_by_eleven(11) == True
assert is_divisible_by_eleven(12) == False