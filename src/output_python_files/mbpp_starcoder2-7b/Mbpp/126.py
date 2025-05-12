"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_common_divisors(a,b):
    """
    >>> sum_common_divisors(10,15)
    6
    """
    return sum(common_divisors(a,b))

def common_divisors(a,b):
    """
    >>> common_divisors(10,15)
    [1, 5]
    """
    return [x for x in range(1,min(a,b)+1) if a%x==0 and b%x==0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_101/01_basics/01_hello_world.py
"""
Write a python function to print "Hello World"
"""

def hello_world():
    """
    >>> hello_world()
    Hello World
    """
    print("Hello World")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_101/01_basics/04_sum_of_digits.py
"""
Write a python function to find the sum of digits of a given number.
assert sum_of_digits(123) == 6
"""

def sum_of_digits(n):
    """
    >>> sum_of_digits(123)
    6
    """
    return sum([int(x) for x in str(n)])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_101/01_basics/02_sum_of_numbers.py
"""
Write a python function to find the sum of numbers from 1 to n.
assert sum_of_numbers(10) == 55
"""

def sum_of_numbers(n):
    """
    >>> sum_of_numbers(10)
    55
    """
    return sum(range(1,n+1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_101/01_basics/03_sum_of_odd_numbers.py
"""
Write a python function to find the sum of odd numbers from 1 to n.
assert sum_of_odd_numbers(10) == 25
"""

def sum_of_odd_numbers(n):
    """
    >>> sum_of_odd_numbers(10)
    25
    """
    return sum(range(1,n+1,2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_101/01_basics/05_sum_of_digits_of_a_number.py
"""
Write a python function to find the sum of digits of a given number.
assert sum_of_digits_of_a_number(123) == 6
"""

def sum_of_digits_of_a_number(n):
    """
    >>> sum_of_digits_of_a_number(123)
    6
    """
    return sum([int(x) for x in str(n)])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_101/01_basics/06_sum_of_digits_of_a_number_using_recursion.py
"""
Write a python function to find the sum of digits of a given number.
assert sum_of_digits_of_a_number_using_recursion(123) == 6
"""

def sum_of_digits_of_a_number_using_recursion(n):
    """
    >>> sum_of_digits_of_a_number_using_recursion(123)
    6
    """
    if n < 10:
        return n
    return n%10 + sum_of_digits_of_a_number_using_recursion(n//10)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_10