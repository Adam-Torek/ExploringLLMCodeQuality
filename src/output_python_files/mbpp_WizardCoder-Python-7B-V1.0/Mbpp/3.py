"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
def is_not_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

# Test cases
print(is_not_prime(2)) # False
print(is_not_prime(4)) # True
print(is_not_prime(7)) # False
print(is_not_prime(15)) # True
print(is_not_prime(17)) # False
print(is_not_prime(23)) # False
print(is_not_prime(29)) # False
print(is_not_prime(31)) # False
print(is_not_prime(47)) # True
print(is_not_prime(56)) # True
print(is_not_prime(89)) # True
print(is_not_prime(97)) # False
print(is_not_prime(101)) # True
print(is_not_prime(103)) # False
print(is_not_prime(107)) # True
print(is_not_prime(109)) # True
print(is_not_prime(113)) # False
print(is_not_prime(127)) # True
print(is_not_prime(131)) # False
print(is_not_prime(137)) # True
print(is_not_prime(149)) # True
print(is_not_prime(151)) # False
print(is_not_prime(157)) # True
print(is_not_prime(163)) # False
print(is_not_prime(167)) # True
print(is_not_prime(173)) # False
print(is_not_prime(179)) # True
print(is_not_prime(181)) # True
print(is_not_prime(191)) # False
print(is_not_prime(193)) # False
print(is_not_prime(197)) # True
print(is_not_prime(199)) # False
print(is_not_prime(209)) # True
print(is_not_prime(211)) # False
print(is_not_prime(223)) # True
print(is_not_prime(227)) # False
print(is_not_prime(233)) # True
print(is_not_prime(239)) # False
print(is_not_prime(241)) # True
print(is_not_prime(251)) # False
print(is_not_prime(257)) # True
print(is_not_prime(263)) # False
print(is_not_prime(269)) # True
print(is_not_prime(271)) # False
print(is_not_prime(277)) # True
print(is_not_prime(281)) # True
print(is_not_prime(283)) # False
print(is_not_prime(293)) # True
print(is_not_prime(307)) # False
print(is_not_prime(311)) # True
print(is_not_prime(313)) # False
print(is_not_prime(317)) # True
print(is_not_prime(331)) # False
print(is_not_prime(337)) # True
print(is_not_prime(347)) # False
print(is_not_prime(349)) # True
print(is_not_prime(353)) # False
print(is_not_prime(359)) # True
print(is_not_prime(367)) # False
print(is_not_prime(3