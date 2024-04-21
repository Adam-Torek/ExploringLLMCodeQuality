def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # Your code here
    return int(round(float(value)))


def is_palindrome(value):
    '''
    Create a function that takes a value (string) and returns True if it
    is a palindrome and False otherwise.

    Examples
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("abc")
    False
    '''
    # Your code here
    return value == value[::-1]


def is_prime(value):
    '''
    Create a function that takes a value (integer) and returns True if it
    is a prime number and False otherwise.

    Examples
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    '''
    # Your code here
    if value == 1:
        return False
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def is_perfect_square(value):
    '''
    Create a function that takes a value (integer) and returns True if it
    is a perfect square and False otherwise.

    Examples
    >>> is_perfect_square(9)
    True
    >>> is_perfect_square(10)
    False
    '''
    # Your code here
    return value ** 0.5 == int(value ** 0.5)


def is_leap_year(value):
    '''
    Create a function that takes a value (integer) and returns True if it
    is a leap year and False otherwise.

    Examples
    >>> is_leap_year(2016)
    True
    >>> is_leap_year(2017)
    False
    '''
    # Your code here
    if value % 4 == 0:
        if value % 100 == 0:
            if value % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_even(value):
    '''
    Create a function that takes a value (integer) and returns True if it
    is even and False otherwise.

    Examples
    >>> is_even(2)
    True
    >>> is_even(1)
    False
    '''
    # Your code here
    return value % 2 == 0


def is_odd(value):
    '''
    Create a function that takes a value (integer) and returns True if it
    is odd and False otherwise.

    Examples
    >>> is_odd(2)
    False
    >>> is_odd(1)
    True
    '''
    # Your code here
    return value % 2 != 0


def is_positive(value):
    '''
    Create a function that takes a value (integer) and returns True if it
    is positive and False otherwise.

    Examples
    >>> is_positive(2)
    True
    >>> is_positive(-1)
    False
    '''
    # Your code here
    return value > 0


def is_negative(value):
    '''
    Create a function that takes a value (integer) and returns True if it
    is negative and False otherwise.

    Examples
    >>> is_negative(2)
    False
    >>> is_negative(-1)
    True
    '''
    # Your code here
    return value < 0


def is_zero