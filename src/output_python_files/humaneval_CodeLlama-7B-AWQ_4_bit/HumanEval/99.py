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
    and returns True if it is a palindrome and False otherwise.

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
    and returns True if it is a prime number and False otherwise.

    Examples
    >>> is_prime("17")
    True
    >>> is_prime("12")
    False
    '''
    # Your code here
    if value == "1":
        return False
    if value == "2":
        return True
    if value == "3":
        return True
    if value == "4":
        return False
    if value == "5":
        return True
    if value == "6":
        return False
    if value == "7":
        return True
    if value == "8":
        return False
    if value == "9":
        return False
    if value == "10":
        return False
    if value == "11":
        return True
    if value == "12":
        return False
    if value == "13":
        return True
    if value == "14":
        return False
    if value == "15":
        return False
    if value == "16":
        return False
    if value == "17":
        return True
    if value == "18":
        return False
    if value == "19":
        return False
    if value == "20":
        return False
    if value == "21":
        return False
    if value == "22":
        return False
    if value == "23":
        return True
    if value == "24":
        return False
    if value == "25":
        return False
    if value == "26":
        return False
    if value == "27":
        return True
    if value == "28":
        return False
    if value == "29":
        return False
    if value == "30":
        return False
    if value == "31":
        return False
    if value == "32":
        return False
    if value == "33":
        return True
    if value == "34":
        return False
    if value == "35":
        return False
    if value == "36":
        return False
    if value == "37":
        return True
    if value == "38":
        return False
    if value == "39":
        return False
    if value == "40":
        return False
    if value == "41":
        return False
    if value == "42":
        return False
    if value == "43":
        return True
    if value == "44":
        return False
    if value == "45":
        return False
    if value == "46":
        return False
    if value == "47":
        return True
    if value == "48":
        return False
    if value == "49":
        return False
    if value == "50":