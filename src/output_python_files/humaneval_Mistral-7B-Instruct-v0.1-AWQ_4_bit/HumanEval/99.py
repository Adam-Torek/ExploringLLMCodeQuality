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
    if value.isdigit():
        return int(value)
    else:
        return round(float(value))


#%%

def closest_integer_test():
    '''
    Test the closest_integer function.
    '''
    for value in ["10", "15.3", "14.5", "-14.5", "0.1", "0.01", "0.001", "1/3", "2/3", "1/4", "3/4"]:
        result = closest_integer(value)
        assert result == int(value) or result == round(float(value))


#%%

def closest_integer_test_rounding():
    '''
    Test the closest_integer function with values that are equidistant
    from two integers.
    '''
    for value in ["14.5", "-14.5", "0.1", "0.01", "0.001", "1/3", "2/3", "1/4", "3/4"]:
        result = closest_integer(value)
        assert result == round(float(value))


#%%

def closest_integer_test_invalid():
    '''
    Test the closest_integer function with invalid input.
    '''
    for value in ["a", "10a", "10.a", "10.0a", "10.00a", "1/0", "1/0a", "1/0.0a", "1/0.00a", "1/0.000a", "1/0.0000a"]:
        result = closest_integer(value)
        assert result == int(value) or result == round(float(value))


#%%

def closest_integer_test_invalid_rounding():
    '''
    Test the closest_integer function with invalid input.
    '''
    for value in ["a", "10a", "10.a", "10.0a", "10.00a", "1/0", "1/0a", "1/0.0a", "1/0.00a", "1/0.000a", "1/0.0000a"]:
        result = closest_integer(value)
        assert result == int(value) or result == round(float(value))


#%%

def closest_integer_test_invalid_rounding_equidistant():
    '''
    Test the closest_integer function with invalid input.
    '''
    for value in ["a", "10a", "10.a", "10.0a", "10.00a", "1/0", "1/0a", "1/0.0a", "1/0.00a", "1/0.000a", "1/0.0000a"]:
        result = closest_integer(value)
        assert result == int(value) or result == round(float(value))


#%%

def closest_integer_test_invalid_rounding_equidistant_rounding():
    '''
    Test the closest_integer function with invalid input.
    '''
    for value in ["a", "10a", "10.a", "10.0a", "10.00a", "1/0", "1/0a", "1/0.0a", "1/0.00a", "1/0.000a", "1/0.000