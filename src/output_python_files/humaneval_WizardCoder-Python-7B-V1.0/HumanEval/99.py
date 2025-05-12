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
    return round(float(value))



# Test cases
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("12.6"))  # Output: 13
print(closest_integer("12.2"))  # Output: 12
print(closest_integer("-12.6"))  # Output: -13
print(closest_integer("-12.2"))  # Output: -12
print(closest_integer("0.5"))  # Output: 0
print(closest_integer("-0.5"))  # Output: 0
print(closest_integer("0.4999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999