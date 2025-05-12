"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""
def divisor(n):
    """
    This function takes an integer n as an argument and returns the number of divisors of n.
    """
    if n == 1:
        return 1
    else:
        count = 1
        for i in range(2, n):
            if n % i == 0:
                count += 1
        return count

# Test the function
assert divisor(15) == 4