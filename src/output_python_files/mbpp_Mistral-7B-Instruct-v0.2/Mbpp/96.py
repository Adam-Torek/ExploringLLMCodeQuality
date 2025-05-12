"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""
from math import sqrt

def divisor(n):
    count = 0
    i = 1
    while i <= int(sqrt(n)):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count

if __name__ == "__main__":
    assert divisor(15) == 4
    print("Test passed!")