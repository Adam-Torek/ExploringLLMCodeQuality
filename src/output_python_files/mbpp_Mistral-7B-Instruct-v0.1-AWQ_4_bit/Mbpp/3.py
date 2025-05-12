"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""

def is_not_prime(n):
    """
    Function to check if a number is not prime
    """
    if n <= 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

assert is_not_prime(2) == False