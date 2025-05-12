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
print(prime_num(15)) # False
print(prime_num(2)) # True
print(prime_num(1)) # False
print(prime_num(7)) # True
print(prime_num(17)) # True
print(prime_num(23)) # True
print(prime_num(29)) # True
print(prime_num(31)) # True
print(prime_num(47)) # True
print(prime_num(53)) # True
print(prime_num(71)) # True
print(prime_num(89)) # True
print(prime_num(101)) # True
print(prime_num(103)) # True
print(prime_num(107)) # True
print(prime_num(109)) # True
print(prime_num(113)) # True
print(prime_num(131)) # True
print(prime_num(137)) # True
print(prime_num(149)) # True
print(prime_num(151)) # True
print(prime_num(163)) # True
print(prime_num(179)) # True
print(prime_num(191)) # True
print(prime_num(193)) # True
print(prime_num(197)) # True
print(prime_num(199)) # True
print(prime_num(233)) # True
print(prime_num(239)) # True
print(prime_num(241)) # True
print(prime_num(257)) # True
print(prime_num(263)) # True
print(prime_num(271)) # True
print(prime_num(283)) # True
print(prime_num(289)) # True
print(prime_num(311)) # True
print(prime_num(313)) # True
print(prime_num(317)) # True
print(prime_num(331)) # True
print(prime_num(337)) # True
print(prime_num(347)) # True
print(prime_num(349)) # True
print(prime_num(353)) # True
print(prime_num(359)) # True
print(prime_num(367)) # True
print(prime_num(373)) # True
print(prime_num(379)) # True
print(prime_num(383)) # True
print(prime_num(389)) # True
print(prime_num(397)) # True
print(prime_num(419)) # True
print(prime_num(431)) # True
print(prime_num(433)) # True
print(prime_num(439)) # True
print(prime_num(443)) # True
print(prime_num(449)) # True
print(prime_num(457)) # True
print(prime_num(461)) # True
print(prime_num(463)) # True
print(prime_num(467)) # True
print(prime_num(479)) # True
print(prime_num(487)) # True
print(prime_num(491)) # True
print(prime_num(499)) # True
print(prime_num(503)) # True
print(prime_num(509)) # True
print(prime_num(521)) # True
print(prime_num(523)) # True
print(prime_num(541)) # True
print(prime_num(547)) # True
print(prime_num(557)) # True
print