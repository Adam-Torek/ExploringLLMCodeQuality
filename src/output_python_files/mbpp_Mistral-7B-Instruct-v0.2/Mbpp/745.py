"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
from functools import reduce

def is_divisible_by_digits(n):
    """
    Check if a number is divisible by every digit it contains
    """
    digits = [int(d) for d in str(n)]
    return all(n % d == 0 for d in digits)

def divisible_by_digits(startnum, endnum):
    """
    Find all numbers between startnum and endnum that are divisible by every digit they contain
    """
    return list(filter(is_divisible_by_digits, range(startnum, endnum+1)))

if __name__ == "__main__":
    assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    print("Test passed")</s>