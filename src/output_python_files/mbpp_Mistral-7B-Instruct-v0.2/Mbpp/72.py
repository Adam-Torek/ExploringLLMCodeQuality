"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
import math

def dif_Square(n):
    """
    :param n: int
    :return: bool
    """
    for i in range(int(math.sqrt(n)), 0, -1):
        if (i * i) - n == (math.sqrt(n) * math.sqrt(n)):
            return True
    return False