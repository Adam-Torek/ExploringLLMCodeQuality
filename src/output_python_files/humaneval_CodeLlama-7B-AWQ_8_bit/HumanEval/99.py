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
    Create a function that takes a value (string) representing a number
    and returns True if it is a palindrome, False otherwise.

    Examples
    >>> is_palindrome("12321")
    True
    >>> is_palindrome("12345")
    False
    '''
    # Your code here
    return value == value[::-1]


def is_prime(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns True if it is a prime number, False otherwise.

    Examples
    >>> is_prime("17")
    True
    >>> is_prime("12")
    False
    '''
    # Your code here
    if value == "1":
        return False
    for i in range(2, int(value)):
        if int(value) % i == 0:
            return False
    return True


def is_perfect_square(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns True if it is a perfect square, False otherwise.

    Examples
    >>> is_perfect_square("16")
    True
    >>> is_perfect_square("17")
    False
    '''
    # Your code here
    return value ** 0.5 == int(value ** 0.5)


def is_perfect_cube(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns True if it is a perfect cube, False otherwise.

    Examples
    >>> is_perfect_cube("8")
    True
    >>> is_perfect_cube("9")
    False
    '''
    # Your code here
    return value ** (1/3) == int(value ** (1/3))


def is_prime_cube(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns True if it is a prime cube, False otherwise.

    Examples
    >>> is_prime_cube("64")
    True
    >>> is_prime_cube("65")
    False
    '''
    # Your code here
    if value == "1":
        return False
    for i in range(2, int(value)):
        if int(value) % i == 0:
            return False
    return value ** (1/3) == int(value ** (1/3))


def is_prime_square(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns True if it is a prime square, False otherwise.

    Examples
    >>> is_prime_square("9")
    True
    >>> is_prime_square("10")
    False
    '''
    # Your code here
    if value == "1":
        return False
    for i in range(2, int(value)):
        if int(value) % i == 0:
            return False
    return value ** 0.5 == int(value ** 0.5)


def is_prime_palindrome(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns True if it is a prime palindrome, False otherwise.

    Examples
    >>> is_prime_palindrome("11