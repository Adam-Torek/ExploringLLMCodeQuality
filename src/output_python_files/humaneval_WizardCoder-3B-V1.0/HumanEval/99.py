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

# Solution:
def closest_integer(value):
    # Convert the string to a float
    num = float(value)

    # Check if the number is equidistant from two integers
    if num.is_integer():
        return int(num)

    # Check if the number is negative
    if num < 0:
        # Find the closest integer to the negative number
        closest_int = -closest_integer(abs(num))
        # If the closest integer is even, round it up
        if closest_int % 2 == 0:
            return closest_int + 1
        else:
            return closest_int
    else:
        # Find the closest integer to the positive number
        closest_int = closest_integer(num)
        # If the closest integer is even, round it down
        if closest_int % 2 == 0:
            return closest_int - 1
        else:
            return closest_int

# Test cases
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15
print(closest_integer("14.5"))  # Output: 15<|endoftext|>