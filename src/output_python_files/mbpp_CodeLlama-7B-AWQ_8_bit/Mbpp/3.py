"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""


def is_not_prime(num):
    """
    Write a python function to identify non-prime numbers.
    assert is_not_prime(2) == False
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False


if __name__ == '__main__':
    print(is_not_prime(2))
    print(is_not_prime(3))
    print(is_not_prime(4))
    print(is_not_prime(5))
    print(is_not_prime(6))
    print(is_not_prime(7))
    print(is_not_prime(8))
    print(is_not_prime(9))
    print(is_not_prime(10))
    print(is_not_prime(11))
    print(is_not_prime(12))
    print(is_not_prime(13))
    print(is_not_prime(14))
    print(is_not_prime(15))
    print(is_not_prime(16))
    print(is_not_prime(17))
    print(is_not_prime(18))
    print(is_not_prime(19))
    print(is_not_prime(20))
    print(is_not_prime(21))
    print(is_not_prime(22))
    print(is_not_prime(23))
    print(is_not_prime(24))
    print(is_not_prime(25))
    print(is_not_prime(26))
    print(is_not_prime(27))
    print(is_not_prime(28))
    print(is_not_prime(29))
    print(is_not_prime(30))
    print(is_not_prime(31))
    print(is_not_prime(32))
    print(is_not_prime(33))
    print(is_not_prime(34))
    print(is_not_prime(35))
    print(is_not_prime(36))
    print(is_not_prime(37))
    print(is_not_prime(38))
    print(is_not_prime(39))
    print(is_not_prime(40))
    print(is_not_prime(41))
    print(is_not_prime(42))
    print(is_not_prime(43))
    print(is_not_prime(44))
    print(is_not_prime(45))
    print(is_not_prime(46))
    print(is_not_prime(47))
    print(is_not_prime(48))
    print(is_not_prime(49))
    print(is_not_prime(50))
    print(is_not_prime(51))
    print(is_not_prime(52))
    print(is_not_prime(53))
    print(is_not_prime(54))
    print(is_not_prime(55))
    print(is_not_prime(56))
    print(is_not_prime(57))
    print(is_not_prime(58))
    print(is_not_prime(59))
    print(is_not_prime(60))
    print(is_not_prime(61))
    print(is_not_prime(62))
    print(is_not_prime(63))
    print(is_not_prime(64))
    print(is_not_prime(65))
    print(is_not_prime(66))
    print(is_not_prime(67))
    print(is_not_prime(68))
    print(is_not_prime(69))
    print(is_not_prime(70))
    print(is_not_