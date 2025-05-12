"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return bell_number(n-1) + bell_number(n-2)

def bell_number_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return bell_number_ways(n-1) + bell_number_ways(n-2) + bell_number_ways(n-1)*bell_number_ways(n-1)

print(bell_number_ways(2))
print(bell_number_ways(3))
print(bell_number_ways(4))
print(bell_number_ways(5))
print(bell_number_ways(6))
print(bell_number_ways(7))
print(bell_number_ways(8))
print(bell_number_ways(9))
print(bell_number_ways(10))
print(bell_number_ways(11))
print(bell_number_ways(12))
print(bell_number_ways(13))
print(bell_number_ways(14))
print(bell_number_ways(15))
print(bell_number_ways(16))
print(bell_number_ways(17))
print(bell_number_ways(18))
print(bell_number_ways(19))
print(bell_number_ways(20))
print(bell_number_ways(21))
print(bell_number_ways(22))
print(bell_number_ways(23))
print(bell_number_ways(24))
print(bell_number_ways(25))
print(bell_number_ways(26))
print(bell_number_ways(27))
print(bell_number_ways(28))
print(bell_number_ways(29))
print(bell_number_ways(30))
print(bell_number_ways(31))
print(bell_number_ways(32))
print(bell_number_ways(33))
print(bell_number_ways(34))
print(bell_number_ways(35))
print(bell_number_ways(36))
print(bell_number_ways(37))
print(bell_number_ways(38))
print(bell_number_ways(39))
print(bell_number_ways(40))
print(bell_number_ways(41))
print(bell_number_ways(42))
print(bell_number_ways(43))
print(bell_number_ways(44))
print(bell_number_ways(45))
print(bell_number_ways(46))
print(bell_number_ways(47))
print(bell_number_ways(48))
print(bell_number_ways(49))
print(bell_number_ways(50))
print(bell_number_ways(51))
print(bell_number_ways(52))
print(bell_number_ways(53))
print(bell_number_ways(54))
print(bell_number_ways(55))
print(bell_number_ways(56))
print(bell_number_ways(57))
print(bell_number_ways(58))
print(bell_number_ways(59))
print(bell_number_ways(60))
print(bell_number_ways(61))
print(bell_number_ways(62))
print(bell_number_ways(63))
print(bell_number_ways(64))
print(bell_number_ways(65))
print(bell_number_ways(66))
print(bell_number_ways(67))
print(bell_number_ways(68))
print(bell_number_ways(69))
print(bell_number_