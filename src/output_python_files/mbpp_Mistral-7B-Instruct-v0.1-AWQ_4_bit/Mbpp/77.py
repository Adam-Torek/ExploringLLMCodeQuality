"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""

def is_divisible_by_11(num):
    """
    This function checks whether a number is divisible by 11 or not.
    """
    if num % 11 == 0:
        return True
    else:
        return False


# Test cases
print(is_divisible_by_11(12345))  # False
print(is_divisible_by_11(11111))  # True
print(is_divisible_by_11(1111))  # False