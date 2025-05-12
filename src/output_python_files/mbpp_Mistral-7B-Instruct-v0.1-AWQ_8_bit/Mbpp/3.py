"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""

def is_not_prime(n):
    """
    This function takes an integer as an input and returns True if the number is not a prime number and False otherwise.
    """
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

assert is_not_prime(2) == False