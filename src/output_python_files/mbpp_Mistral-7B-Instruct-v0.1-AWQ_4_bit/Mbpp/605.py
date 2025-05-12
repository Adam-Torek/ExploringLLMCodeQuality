"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""

def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True