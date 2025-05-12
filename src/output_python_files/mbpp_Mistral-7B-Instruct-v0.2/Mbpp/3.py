"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
def is_not_prime(n):
    """
    This function returns True if the given number is not a prime number.
    """
    if n <= 1:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False

assert is_not_prime(2) == False
assert is_not_prime(4) == True
assert is_not_prime(15) == True
assert is_not_prime(17) == False
assert is_not_prime(20) == True
assert is_not_prime(29) == False
assert is_not_prime(30) == True
assert is_not_prime(101) == False
assert is_not_prime(102) == True