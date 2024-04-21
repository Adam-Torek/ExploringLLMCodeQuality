"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""

def is_not_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

# Test cases
print(is_not_prime(2)) # False
print(is_not_prime(3)) # True
print(is_not_prime(4)) # False
print(is_not_prime(5)) # True
print(is_not_prime(6)) # False
print(is_not_prime(7)) # True
print(is_not_prime(8)) # False
print(is_not_prime(9)) # True
print(is_not_prime(10)) # False<|endoftext|>