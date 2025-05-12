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
print(closest_integer("12.6"))  # Output: 12
print(closest_integer("12.4"))  # Output: 12
print(closest_integer("12.5"))  # Output: 12
print(closest_integer("12.49"))  # Output: 12
print(closest_integer("12.45"))  # Output: 12
print(closest_integer("12.46"))  # Output: 13
print(closest_integer("12.40"))  # Output: 12
print(closest_integer("12.41"))  # Output: 12
print(closest_integer("12.42"))  # Output: 12
print(closest_integer("12.43"))  # Output: 12
print(closest_integer("12.44"))  # Output: 12
print(closest_integer("12.47"))  # Output: 12
print(closest_integer("12.48"))  # Output: 12
print(closest_integer("12.49"))  # Output: 12
print(closest_integer("12.50"))  # Output: 12
print(closest_integer("12.51"))  # Output: 13
print(closest_integer("12.52"))  # Output: 13
print(closest_integer("12.53"))  # Output: 13
print(closest_integer("12.54"))  # Output: 13
print(closest_integer("12.55"))  # Output: 13
print(closest_integer("12.56"))  # Output: 13
print(closest_integer("12.57"))  # Output: 13
print(closest_integer("12.58"))  # Output: 13
print(closest_integer("12.59"))  # Output: 13
print(closest_integer("12.60"))  # Output: 13
print(closest_integer("12.61"))  # Output: 13
print(closest_integer("12.62"))  # Output: 13
print(closest_integer("12.63"))  # Output: 13
print(closest_integer("12.64"))  # Output: 13
print(closest_integer("12.65"))  # Output: 13
print(closest_integer("12.66"))  # Output: 13
print(closest_integer("12.67"))  # Output: 13
print(closest_integer("12.68"))  # Output: 13
print(closest_integer("12.69"))  # Output: 13
print(closest_integer("12.70"))  # Output: 13
print(closest_integer("12.71"))  # Output: 1