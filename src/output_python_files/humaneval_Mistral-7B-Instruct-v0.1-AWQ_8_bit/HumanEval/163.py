def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    digits = []
    for i in range(a, b+1):
        if i % 10 == 0:
            digits.append(i)
    return digits


def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_even_digits(2, 8) => [2, 4, 6, 8]
    generate_even_digits(8, 2) => [2, 4, 6, 8]
    generate_even_digits(10, 14) => []
    """
    digits = []
    for i in range(a, b+1):
        if i % 10 == 0 and i % 2 == 0:
            digits.append(i)
    return digits


def generate_odd_digits(a, b):
    """
    Given two positive integers a and b, return the odd digits between a
    and b, in ascending order.

    For example:
    generate_odd_digits(2, 8) => [1, 3, 5, 7]
    generate_odd_digits(8, 2) => [1, 3, 5, 7]
    generate_odd_digits(10, 14) => [1, 3, 5, 7, 9, 11, 13]
    """
    digits = []
    for i in range(a, b+1):
        if i % 10 == 0 and i % 2 != 0:
            digits.append(i)
    return digits


def generate_even_and_odd_digits(a, b):
    """
    Given two positive integers a and b, return the even digits and odd digits
    between a and b, in ascending order.

    For example:
    generate_even_and_odd_digits(2, 8) => [2, 4, 6, 8, 1, 3, 5, 7]
    generate_even_and_odd_digits(8, 2) => [2, 4, 6, 8, 1, 3, 5, 7]
    generate_even_and_odd_digits(10, 14) => [2, 4, 6, 8, 1, 3, 5, 7, 9, 11, 13]
    """
    even_digits = generate_even_digits(a, b)
    odd_digits = generate_odd_digits(a, b)
    digits = even_digits + odd_digits
    return digits