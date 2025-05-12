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
    roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    result = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result.lower()


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in uppercase.
    Restrictions: 1 <= num <= 3999

    Examples:
    >>> int_to_roman(19) == 'XIX'
    >>> int_to_roman(152) == 'CLIV'
    >>> int_to_roman(426) == 'CDXXVI'
    """
    roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result.upper()


def main():
    num = int(input("Enter a number between 1 and 1000: "))
    if 1 <= num <= 100:
        print(int_to_mini_roman(num))
    elif 1 <= num <= 3999:
        print(int_to_roman(num))
    else:
        print("Invalid input. Please enter a number between 1 and 3999.")

if __name__ == "__main__":
    main()