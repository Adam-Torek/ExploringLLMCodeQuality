"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""


def armstrong_number(number):
    """
    >>> armstrong_number(153)
    True
    >>> armstrong_number(123)
    False
    """
    number = str(number)
    length = len(number)
    sum = 0
    for digit in number:
        sum += int(digit) ** length
    return sum == number


if __name__ == "__main__":
    import doctest

    doctest.testmod()