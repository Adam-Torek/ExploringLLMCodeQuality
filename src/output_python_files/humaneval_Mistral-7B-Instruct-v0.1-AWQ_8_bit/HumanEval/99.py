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
    # convert string to float
    value = float(value)

    # find closest integer
    closest_int = round(value)

    # check if closest integer is equidistant from two integers
    if closest_int == round(value, 0) and closest_int == round(value, 1):
        # round away from zero
        if closest_int > 0:
            closest_int += 1
        else:
            closest_int -= 1

    return closest_int


# test function
print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))