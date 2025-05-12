"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""

def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    i = 1
    while i * i <= n:
        if n % i == 0:
            return True
        i += 1
    return False