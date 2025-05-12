"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
import math

def is_prime(num):
    """
    Helper function to check if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def count_Primes_nums(n):
    """
    Function to count the number of prime numbers less than n
    """
    count = 0
    for i in range(2, n+1):
        if is_prime(i):
            count += 1
    return count