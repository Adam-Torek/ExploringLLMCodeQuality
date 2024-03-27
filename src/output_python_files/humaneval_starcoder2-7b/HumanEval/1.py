from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
<file_sep>/python/recursion/fibonacci.py
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
<file_sep>/python/recursion/reverse_string.py
def reverse_string(s):
    """
    Return the reverse of the string s.
    >>> reverse_string('abc')
    'cba'
    >>> reverse_string('a')
    'a'
    >>> reverse_string('madam')
   'madam'
    >>> reverse_string('123456789')
    '987654321'
    """
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
<file_sep>/python/recursion/sum_digits.py
def sum_digits(n):
    """
    Return the sum of the digits of positive integer n.
    >>> sum_digits(23)
    5
    >>> sum_digits(496)
    19
    >>> sum_digits(1234567890)
    45
    """
    if n < 10:
        return n
    else:
        return sum_digits(n // 10) + n % 10
<file_sep>/python/recursion/reverse_list.py
def reverse_list(lst):
    """
    Return a new list that is the reverse of lst.
    >>> reverse_list([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse_list([3, 1, 5, 4])
    [4, 5, 1, 3]
    >>> reverse_list([])
    []
    """
    if len(lst) == 0:
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]
<file_sep>/python/recursion/sum_list.py
def sum_list(lst):
    """
    Return the sum of the numbers in the list lst.
    >>> sum_list([1, 10])
    11
    >>> sum_list([1, -2, 3])
    2
    >>> sum_list([])
    0
    """
    if len(lst) == 0:
        return 0
    else:
        return sum_list(lst[1:]) + lst[0]
<file_sep>/python/recursion/factorial.py
def factorial(n):
    """
    Return n factorial.
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n
<file_sep>/python/recursion/sum_of_squares.py
def sum_of_squares(n):
    """
    Return the sum of the squares of the numbers from 1 to n.
    >>> sum_of_squares(2)
    5
    >>> sum_of_squares(3)
    14
    >>> sum_of_squares(10)
    385
    """
    if n == 1:
        return 1
    else:
        return sum_of_squares(n - 1) + n ** 2
<file_sep>/python/recursion/sum_of_n.py
def sum_of_n(n):
    """
    Return the sum of 1 + 2 + 3 +... + n.
    >>> sum