"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""

def newman_prime(n):
    """
    Returns the nth newman-shanks-williams prime number.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return 5 * newman_prime(n-1) + 2

# Test the function
assert newman_prime(3) == 7<|endoftext|>