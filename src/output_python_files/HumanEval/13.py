def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    """
    return a * b // greatest_common_divisor(a, b)


def is_prime(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    >>> is_prime(15)
    False
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    >>> is_prime(21)
    True
    >>> is_prime(22)
    False
    >>> is_prime(23)
    True
    >>> is_prime(24)
    False
    >>> is_prime(25)
    False
    >>> is_prime(26)
    False
    >>> is_prime(27)
    True
    >>> is_prime(28)
    False
    >>> is_prime(29)
    True
    >>> is_prime(30)
    False
    >>> is_prime(31)
    True
    >>> is_prime(32)
    False
    >>> is_prime(33)
    True
    >>> is_prime(34)
    False
    >>> is_prime(35)
    False
    >>> is_prime(36)
    False
    >>> is_prime(37)
    True
    >>> is_prime(38)
    False
    >>> is_prime(39)
    True
    >>> is_prime(40)
    False
    >>> is_prime(41)
    True
    >>> is_prime(42)
    False
    >>> is_prime(43)
    True
    >>> is_prime(44)
    False
    >>> is_prime(45)
    False
    >>> is_prime(46)
    False
    >>> is_prime(47)
    True
    >>> is_prime(48)
    False
    >>> is_prime(49)
    True
    >>> is_prime(50)
    False
    >>> is_prime(51)
    True
    >>> is_prime(52)
    False
    >>> is_prime(53)
    True
    >>> is_prime(54)
    False
    >>> is_prime(55)
    False
    >>> is_prime(56)
    False
    >>> is_prime(57)
    True
    >>> is_prime(58)
    False
    >>> is_prime(59)
    True
    >>> is_prime(60)
    False
    >>> is_prime(