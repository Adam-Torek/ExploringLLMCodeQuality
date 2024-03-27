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
        if (i * i - n) < 0:
            continue
        elif (math.sqrt(i * i - n) % 1) != 0:
            continue
        else:
            return True
    return False</s>