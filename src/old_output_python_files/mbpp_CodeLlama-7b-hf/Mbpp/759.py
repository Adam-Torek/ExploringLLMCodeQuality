"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""


def is_decimal(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(is_decimal('123.11'))
    print(is_decimal('123.111'))
    print(is_decimal('123.1111'))
    print(is_decimal('123.11111'))
    print(is_decimal('123.111111'))
    print(is_decimal('123.1111111'))
    print(is_decimal('123.11111111'))
    print(is_decimal('123.111111111'))
    print(is_decimal('123.1111111111'))
    print(is_decimal('123.11111111111'))
    print(is_decimal('123.111111111111'))
    print(is_decimal('123.1111111111111'))
    print(is_decimal('123.11111111111111'))
    print(is_decimal('123.111111111111111'))
    print(is_decimal('123.1111111111111111'))
    print(is_decimal('123.11111111111111111'))
    print(is_decimal('123.111111111111111111'))
    print(is_decimal('123.1111111111111111111'))
    print(is_decimal('123.11111111111111111111'))
    print(is_decimal('123.111111111111111111111'))
    print(is_decimal('123.1111111111111111111111'))
    print(is_decimal('123.11111111111111111111111'))
    print(is_decimal('123.111111111111111111111111'))
    print(is_decimal('123.1111111111111111111111111'))
    print(is_decimal('123.11111111111111111111111111'))
    print(is_decimal('123.111111111111111111111111111'))
    print(is_decimal('123.1111111111111111111111111111'))
    print(is_decimal('123.11111111111111111111111111111'))
    print(is_decimal('123.111111111111111111111111111111'))
    print(is_decimal('123.1111111111111111111111111111111'))
    print(is_decimal('123.111111