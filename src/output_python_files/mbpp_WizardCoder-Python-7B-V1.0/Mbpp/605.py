"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
def prime_num(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(prime_num(13)) # True
print(prime_num(14)) # False
print(prime_num(23)) # True
print(prime_num(1)) # False
print(prime_num(2)) # True
print(prime_num(3)) # True
print(prime_num(4)) # False
print(prime_num(5)) # True
print(prime_num(7)) # True
print(prime_num(8)) # False
print(prime_num(9)) # False
print(prime_num(11)) # True
print(prime_num(12)) # False
print(prime_num(17)) # True
print(prime_num(19)) # True
print(prime_num(29)) # True
print(prime_num(31)) # True
print(prime_num(47)) # True
print(prime_num(53)) # True
print(prime_num(67)) # True
print(prime_num(71)) # True
print(prime_num(89)) # True
print(prime_num(97)) # True
print(prime_num(101)) # False
print(prime_num(103)) # True
print(prime_num(107)) # True
print(prime_num(109)) # False
print(prime_num(113)) # True
print(prime_num(127)) # True
print(prime_num(131)) # False
print(prime_num(137)) # True
print(prime_num(149)) # True
print(prime_num(151)) # False
print(prime_num(157)) # True
print(prime_num(163)) # True
print(prime_num(173)) # True
print(prime_num(179)) # True
print(prime_num(181)) # False
print(prime_num(191)) # True
print(prime_num(193)) # True
print(prime_num(197)) # True
print(prime_num(199)) # False
print(prime_num(209)) # True
print(prime_num(211)) # False
print(prime_num(223)) # True
print(prime_num(227)) # True
print(prime_num(233)) # True
print(prime_num(239)) # True
print(prime_num(241)) # False
print(prime_num(251)) # True
print(prime_num(257)) # True
print(prime_num(263)) # True
print(prime_num(269)) # False
print(prime_num(271)) # True
print(prime_num(277)) # True
print(prime_num(281)) # False
print(prime_num(283)) # True
print(prime_num(293)) # True
print(prime_num(307)) # True
print(prime_num(311)) # False
print(prime_num(313)) # True
print(prime_num(317)) # True
print(prime_num(331)) # True
print(prime_num(337)) # True
print(prime_num(347)) # True
print(prime_num(349)) # False
print(prime_num(353)) # True
print(prime_num(359)) # True
print(prime_num(367)) # True
print(prime_num(373)) # True
print(prime_num(379)) # False
print(prime_num(383)) # True
print(prime_num(389)) # True
print(prime_