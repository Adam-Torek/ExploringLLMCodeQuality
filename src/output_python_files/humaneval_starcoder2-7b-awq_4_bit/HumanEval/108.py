def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count

def sum_digits(num):
    """
    Write a function sum_digits which takes an integer and returns the sum of
    its digits.
    >>> sum_digits(123) == 6
    >>> sum_digits(12345) == 15
    >>> sum_digits(1234567890) == 45
    """
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num // 10)

def sum_digits(num):
    """
    Write a function sum_digits which takes an integer and returns the sum of
    its digits.
    >>> sum_digits(123) == 6
    >>> sum_digits(12345) == 15
    >>> sum_digits(1234567890) == 45
    """
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num // 10)

def sum_digits(num):
    """
    Write a function sum_digits which takes an integer and returns the sum of
    its digits.
    >>> sum_digits(123) == 6
    >>> sum_digits(12345) == 15
    >>> sum_digits(1234567890) == 45
    """
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num // 10)

def sum_digits(num):
    """
    Write a function sum_digits which takes an integer and returns the sum of
    its digits.
    >>> sum_digits(123) == 6
    >>> sum_digits(12345) == 15
    >>> sum_digits(1234567890) == 45
    """
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num // 10)

def sum_digits(num):
    """
    Write a function sum_digits which takes an integer and returns the sum of
    its digits.
    >>> sum_digits(123) == 6
    >>> sum_digits(12345) == 15
    >>> sum_digits(1234567890) == 45
    """
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num //