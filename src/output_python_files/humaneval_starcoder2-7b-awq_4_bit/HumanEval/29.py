from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

# BEGIN SOLUTION
    return [s for s in strings if s.startswith(prefix)]
# END SOLUTION


def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/01-basics/01-hello-world/hello_world.py
"""
Write a function that prints "Hello, World!" to the console.
"""


def hello_world():
    """
    >>> hello_world()
    Hello, World!
    """

# BEGIN SOLUTION
    print("Hello, World!")
# END SOLUTION


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/01-basics/03-sum-of-digits/sum_of_digits.py
"""
Write a function that takes a positive integer and returns the sum of its digits.
"""


def sum_of_digits(n: int) -> int:
    """
    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(1000)
    1
    >>> sum_of_digits(1234567890)
    45
    """

# BEGIN SOLUTION
    return sum([int(c) for c in str(n)])
# END SOLUTION


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/01-basics/02-sum-of-squares/sum_of_squares.py
"""
Write a function that takes a positive integer and returns the sum of its squares.
"""


def sum_of_squares(n: int) -> int:
    """
    >>> sum_of_squares(1)
    1
    >>> sum_of_squares(2)
    5
    >>> sum_of_squares(3)
    14
    """

# BEGIN SOLUTION
    return sum([i**2 for i in range(1, n+1)])
# END SOLUTION


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/01-basics/04-sum-of-digits-in-string/sum_of_digits_in_string.py
"""
Write a function that takes a string and returns the sum of its digits.
"""


def sum_of_digits_in_string(s: str) -> int:
    """
    >>> sum_of_digits_in_string("123")
    6
    >>> sum_of_digits_in_string("1000")
    1
    >>> sum_of_digits_in_string("1234567890")
    45
    """

# BEGIN SOLUTION
    return sum([int(c) for c in s if c.isdigit()])
# END SOLUTION


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/01-basics/05-sum-of-digits-in-string-2/sum_of_digits_in_string_2.py
"""
Write a function that takes a string and returns the sum of its digits.
"""


def sum_of_digits_in_string_2(s: str) -> int:
    """
    >>> sum_of_digits_in_string_2("123")
    6
    >>> sum_of_digits_in_string_2("1000")
    1
    >>> sum_of_digits_in_string_2("1234567890")
    45
    """

# BEGIN SOLUTION
    return sum([int(c) for c in s if c.isdigit()])
# END SOLUTION


if __name__ == '__main__':
    import doctest