"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""

def dif_Square(n):
    for i in range(1, n):
        for j in range(i+1, n):
            if n == i**2 - j**2:
                return True
    return False