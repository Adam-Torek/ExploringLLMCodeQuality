"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
def is_not_prime(num):
    if num < 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

# Test cases
print(is_not_prime(2)) # False
print(is_not_prime(7)) # False
print(is_not_prime(13)) # False
print(is_not_prime(17)) # False
print(is_not_prime(19)) # False
print(is_not_prime(23)) # False
print(is_not_prime(29)) # False
print(is_not_prime(31)) # False
print(is_not_prime(37)) # False
print(is_not_prime(41)) # False
print(is_not_prime(43)) # False
print(is_not_prime(47)) # False
print(is_not_prime(53)) # False
print(is_not_prime(59)) # False
print(is_not_prime(61)) # False
print(is_not_prime(67)) # False
print(is_not_prime(71)) # False
print(is_not_prime(73)) # False
print(is_not_prime(79)) # False
print(is_not_prime(83)) # False
print(is_not_prime(89)) # False
print(is_not_prime(97)) # False
print(is_not_prime(101)) # False
print(is_not_prime(103)) # False
print(is_not_prime(107)) # False
print(is_not_prime(109)) # False
print(is_not_prime(113)) # False
print(is_not_prime(127)) # False
print(is_not_prime(131)) # False
print(is_not_prime(137)) # False
print(is_not_prime(149)) # False
print(is_not_prime(151)) # False
print(is_not_prime(157)) # False
print(is_not_prime(163)) # False
print(is_not_prime(167)) # False
print(is_not_prime(173)) # False
print(is_not_prime(179)) # False
print(is_not_prime(181)) # False
print(is_not_prime(191)) # False
print(is_not_prime(193)) # False
print(is_not_prime(197)) # False
print(is_not_prime(199)) # False
print(is_not_prime(211)) # False
print(is_not_prime(223)) # False
print(is_not_prime(227)) # False
print(is_not_prime(233)) # False
print(is_not_prime(239)) # False
print(is_not_prime(241)) # False
print(is_not_prime(251)) # False
print(is_not_prime(257)) # False
print(is_not_prime(263)) # False
print(is_not_prime(269)) # False
print(is_not_prime(271)) # False
print(is_not_prime(277)) # False
print(is_not_prime(281)) # False
print(is_not_prime(283)) # False
print(is_not_prime(293)) # False
print(is_not_prime(307)) # False
print(is_not_prime(311)) # False
print(is_not_prime(313)) # False
print(is