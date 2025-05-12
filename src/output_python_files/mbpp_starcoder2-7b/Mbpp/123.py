"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""

def amicable_numbers_sum(n):
    """
    >>> amicable_numbers_sum(999)
    504
    """
    return sum(amicable_numbers(n))

def amicable_numbers(n):
    """
    >>> amicable_numbers(999)
    [220, 284]
    """
    amicable_numbers = []
    for i in range(1, n):
        if is_amicable(i):
            amicable_numbers.append(i)
    return amicable_numbers

def is_amicable(n):
    """
    >>> is_amicable(220)
    True
    >>> is_amicable(284)
    True
    >>> is_amicable(100)
    False
    """
    return sum(proper_divisors(n)) == n and sum(proper_divisors(sum(proper_divisors(n)))) == n and n!= sum(proper_divisors(n))

def proper_divisors(n):
    """
    >>> proper_divisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> proper_divisors(284)
    [1, 2, 4, 71, 142]
    """
    proper_divisors = []
    for i in range(1, n):
        if n % i == 0:
            proper_divisors.append(i)
    return proper_divisors

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/project_euler/problem_001.py
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples_sum(n):
    """
    >>> multiples_sum(10)
    23
    >>> multiples_sum(1000)
    233168
    """
    return sum(multiples(n))

def multiples(n):
    """
    >>> multiples(10)
    [3, 5, 6, 9]
    >>> multiples(1000)
    [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99, 100, 102, 105, 108, 110, 111, 114, 115, 117, 120, 123, 125, 126, 129, 130, 132, 135, 138, 140, 141, 144, 145, 147, 150, 153, 155, 156, 159, 160, 162, 165, 168, 170, 171, 174, 175, 177, 180, 183,