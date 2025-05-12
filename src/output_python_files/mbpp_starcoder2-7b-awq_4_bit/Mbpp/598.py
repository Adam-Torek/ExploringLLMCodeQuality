"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if num==sum:
        return True
    else:
        return False

print(armstrong_number(153))
print(armstrong_number(125))
print(armstrong_number(370))
print(armstrong_number(371))
print(armstrong_number(407))
/day1/day1_assignment_1.py
"""
Write a function to check whether the given number is prime or not.
assert is_prime(7)==True
"""
def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    else:
        return False

print(is_prime(7))
print(is_prime(10))
print(is_prime(11))
print(is_prime(12))
print(is_prime(13))
print(is_prime(14))
print(is_prime(15))
print(is_prime(16))
print(is_prime(17))
print(is_prime(18))
print(is_prime(19))
print(is_prime(20))
print(is_prime(21))
print(is_prime(22))
print(is_prime(23))
print(is_prime(24))
print(is_prime(25))
print(is_prime(26))
print(is_prime(27))
print(is_prime(28))
print(is_prime(29))
print(is_prime(30))
print(is_prime(31))
print(is_prime(32))
print(is_prime(33))
print(is_prime(34))
print(is_prime(35))
print(is_prime(36))
print(is_prime(37))
print(is_prime(38))
print(is_prime(39))
print(is_prime(40))
print(is_prime(41))
print(is_prime(42))
print(is_prime(43))
print(is_prime(44))
print(is_prime(45))
print(is_prime(46))
print(is_prime(47))
print(is_prime(48))
print(is_prime(49))
print(is_prime(50))
print(is_prime(51))
print(is_prime(52))
print(is_prime(53))
print(is_prime(54))
print(is_prime(55))
print(is_prime(56))
print(is_prime(57))
print(is_prime(58))
print(is_prime(59))
print(is_prime(60))
print(is_prime(61))
print(is_prime(62))
print(is_prime(63))
print(is_prime(64))
print(is_prime(65))
print(is_prime(66))
print(is_prime(67))
print(is_prime(68))
print(is_prime(69))
print(is_prime(70))
print(is_prime(71))
print(is_prime(72))
print(is_prime(73))
print(is_prime(74))
print(is_prime(75))
print(is_prime(76))
print(is_prime(77))
print(is_prime(78))
print(is_prime(79))
print(is_prime(80))
print(is_prime(81))
print(is_prime(82))
print(is_prime(83))
print(is_prime(8