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
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = ''
    number = abs(number)
    while number > 0:
        if number >= roman_dict['M']:
            result += roman_dict['M']
            number -= roman_dict['M']
        elif number >= roman_dict['D']:
            result += roman_dict['D']
            number -= roman_dict['D']
        elif number >= roman_dict['C']:
            result += roman_dict['C']
            number -= roman_dict['C']
        elif number >= roman_dict['L']:
            result += roman_dict['L']
            number -= roman_dict['L']
        elif number >= roman_dict['X']:
            result += roman_dict['X']
            number -= roman_dict['X']
        elif number >= roman_dict['V']:
            result += roman_dict['V']
            number -= roman_dict['V']
        else:
            result += roman_dict['I']
            number -= roman_dict['I']
    return result.lower()


if __name__ == '__main__':
    print(int_to_mini_roman(19))
    print(int_to_mini_roman(152))
    print(int_to_mini_roman(426))