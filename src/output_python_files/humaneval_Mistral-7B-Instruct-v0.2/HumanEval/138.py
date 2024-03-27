def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    for i in range(int(n/2), 0, -2):
        if n - i - i - i - i == 0:
            return True
    return False

# test
print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(10))
print(is_equal_to_sum_even(12))
print(is_equal_to_sum_even(14))
print(is_equal_to_sum_even(16))
print(is_equal_to_sum_even(18))
print(is_equal_to_sum_even(20))
print(is_equal_to_sum_even(22))
print(is_equal_to_sum_even(24))
print(is_equal_to_sum_even(26))
print(is_equal_to_sum_even(28))
print(is_equal_to_sum_even(30))
print(is_equal_to_sum_even(32))
print(is_equal_to_sum_even(34))
print(is_equal_to_sum_even(36))
print(is_equal_to_sum_even(38))
print(is_equal_to_sum_even(40))
print(is_equal_to_sum_even(42))
print(is_equal_to_sum_even(44))
print(is_equal_to_sum_even(46))
print(is_equal_to_sum_even(48))
print(is_equal_to_sum_even(50))
print(is_equal_to_sum_even(52))
print(is_equal_to_sum_even(54))
print(is_equal_to_sum_even(56))
print(is_equal_to_sum_even(58))
print(is_equal_to_sum_even(60))
print(is_equal_to_sum_even(62))
print(is_equal_to_sum_even(64))
print(is_equal_to_sum_even(66))
print(is_equal_to_sum_even(68))
print(is_equal_to_sum_even(70))
print(is_equal_to_sum_even(72))
print(is_equal_to_sum_even(74))
print(is_equal_to_sum_even(76))
print(is_equal_to_sum_even(78))
print(is_equal_to_sum_even(80))
print(is_equal_to_sum_even(82))
print(is_equal_to_sum_even(84))
print(is_equal_to_sum_even(86))
print(is_equal_to_sum_even(88))
print(is_equal_to_sum_even(90))
print(is_equal_to_sum_even(92))
print(is_equal_to_sum_even(94))
print(is_equal_to_sum_even(96))
print(is_equal_to_sum_even(98))
print(is_equal_to_sum_even(100))
print(is_equal_to_sum_even(102))
print(is_equal_to_sum_even(104))
print(is_equal_to_sum_even(106))
print(is_equal_to_sum_even(108))
print(is_equal_to_sum_even(110))
print