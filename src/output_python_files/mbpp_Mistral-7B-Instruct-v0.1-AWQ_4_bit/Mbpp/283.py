"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""

def validate(n):
    """
    :type n: int
    :rtype: bool
    """
    digits = [int(d) for d in str(n)]
    for i in range(10):
        if digits[i] > i:
            return False
    return True