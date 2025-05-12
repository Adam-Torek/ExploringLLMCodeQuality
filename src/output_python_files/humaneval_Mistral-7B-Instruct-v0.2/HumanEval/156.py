def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x',
        40: 'xl', 50: 'l', 90: 'xc', 100: 'c',
        400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    roman_numeral = ''
    while number > 0:
        for i in reversed(range(10)):
            power = 10 ** (i + 1)
            if number >= power:
                roman_numeral += roman_numerals[power]
                number -= power
                break
    return roman_numeral


if __name__ == '__main__':
    import doctest
    doctest.testmod()