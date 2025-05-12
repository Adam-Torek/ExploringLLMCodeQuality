def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def is_prime(num):
    """Given an integer, return True if the number is prime and False otherwise.

    A prime number is a number that is only evenly divisible by itself and 1.

    Note: 0 and 1 are NOT considered prime numbers

    Example:
        is_prime(1) ==> False
        is_prime(2) ==> True
        is_prime(-3) ==> False
    """

def is_palindrome(num):
    """Given an integer, return True if the number is palindrome and False otherwise.

    A palindrome is a number that is the same forwards and backwards

    Example:
        is_palindrome(121) ==> True
        is_palindrome(221) ==> False
        is_palindrome(0) ==> True
    """

def is_armstrong(num):
    """Given an integer, return True if the number is an Armstrong number and False otherwise.

    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    Example:
        is_armstrong(1) ==> True
        is_armstrong(371) ==> True
        is_armstrong(9474) ==> True
        is_armstrong(93084) ==> True
        is_armstrong(54748) ==> True
        is_armstrong(2) ==> True
        is_armstrong(3) ==> False
    """

def is_perfect(num):
    """Given an integer, return True if the number is perfect and False otherwise.

    A perfect number is a number that is equal to the sum of its positive divisors, excluding the number itself.

    Example:
        is_perfect(6) ==> True # 1, 2, 3
        is_perfect(28) ==> True # 1, 2, 4, 7, 14
        is_perfect(7) ==> False
    """

def is_abundant(num):
    """Given an integer, return True if the number is abundant and False otherwise.

    An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.

    Example:
        is_abundant(12) ==> True # 1, 2, 3, 4, 6
        is_abundant(10) ==> False
    """

def is_deficient(num):
    """Given an integer, return True if the number is deficient and False otherwise.

    A deficient number or lacking number is a number for which the sum of its proper divisors is less than the number itself.

    Example:
        is_deficient(12) ==> False # 1, 2, 3, 4, 6
        is_deficient(10) ==> True
    """

def is_happy(num):
    """Given an integer, return True if the number is happy and False otherwise.

    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

    Example:
        is_happy(