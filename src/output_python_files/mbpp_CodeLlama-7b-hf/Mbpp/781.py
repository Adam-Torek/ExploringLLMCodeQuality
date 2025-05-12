"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""


def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


if __name__ == '__main__':
    print(count_divisors(10))
    print(count_divisors(12))
    print(count_divisors(15))
    print(count_divisors(16))
    print(count_divisors(17))
    print(count_divisors(18))
    print(count_divisors(19))
    print(count_divisors(20))
    print(count_divisors(21))
    print(count_divisors(22))
    print(count_divisors(23))
    print(count_divisors(24))
    print(count_divisors(25))
    print(count_divisors(26))
    print(count_divisors(27))
    print(count_divisors(28))
    print(count_divisors(29))
    print(count_divisors(30))
    print(count_divisors(31))
    print(count_divisors(32))
    print(count_divisors(33))
    print(count_divisors(34))
    print(count_divisors(35))
    print(count_divisors(36))
    print(count_divisors(37))
    print(count_divisors(38))
    print(count_divisors(39))
    print(count_divisors(40))
    print(count_divisors(41))
    print(count_divisors(42))
    print(count_divisors(43))
    print(count_divisors(44))
    print(count_divisors(45))
    print(count_divisors(46))
    print(count_divisors(47))
    print(count_divisors(48))
    print(count_divisors(49))
    print(count_divisors(50))
    print(count_divisors(51))
    print(count_divisors(52))
    print(count_divisors(53))
    print(count_divisors(54))
    print(count_divisors(55))
    print(count_divisors(56))
    print(count_divisors(57))
    print(count_divisors(58))
    print(count_divisors(59))
    print(count_divisors(60))
    print(count_divisors(61))
    print(count_divisors(62))
    print(count_divisors(63))
    print(count_divisors(64))
    print(count_divisors(65))
    print(count_divisors(66))
    print(count_divisors(67))
    print(count_divisors(68))
    print(count_divisors(69))
    print(count_divisors(70))
    print(count_divisors(71))
    print(count_divisors(72))
    print(count_divisors(73))
    print(count_divisors(74))
    print(count_divisors(75))
    print(count_