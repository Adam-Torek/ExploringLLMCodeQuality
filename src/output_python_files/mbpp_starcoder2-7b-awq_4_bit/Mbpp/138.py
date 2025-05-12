"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""

def is_Sum_Of_Powers_Of_Two(num):
    if num == 0:
        return True
    while num > 0:
        if num & 1 == 1:
            return False
        num = num >> 1
    return True

print(is_Sum_Of_Powers_Of_Two(10))
print(is_Sum_Of_Powers_Of_Two(15))
print(is_Sum_Of_Powers_Of_Two(16))
print(is_Sum_Of_Powers_Of_Two(17))
print(is_Sum_Of_Powers_Of_Two(18))
print(is_Sum_Of_Powers_Of_Two(19))
print(is_Sum_Of_Powers_Of_Two(20))
print(is_Sum_Of_Powers_Of_Two(21))
print(is_Sum_Of_Powers_Of_Two(22))
print(is_Sum_Of_Powers_Of_Two(23))
print(is_Sum_Of_Powers_Of_Two(24))
print(is_Sum_Of_Powers_Of_Two(25))
print(is_Sum_Of_Powers_Of_Two(26))
print(is_Sum_Of_Powers_Of_Two(27))
print(is_Sum_Of_Powers_Of_Two(28))
print(is_Sum_Of_Powers_Of_Two(29))
print(is_Sum_Of_Powers_Of_Two(30))
print(is_Sum_Of_Powers_Of_Two(31))
print(is_Sum_Of_Powers_Of_Two(32))
print(is_Sum_Of_Powers_Of_Two(33))
print(is_Sum_Of_Powers_Of_Two(34))
print(is_Sum_Of_Powers_Of_Two(35))
print(is_Sum_Of_Powers_Of_Two(36))
print(is_Sum_Of_Powers_Of_Two(37))
print(is_Sum_Of_Powers_Of_Two(38))
print(is_Sum_Of_Powers_Of_Two(39))
print(is_Sum_Of_Powers_Of_Two(40))
print(is_Sum_Of_Powers_Of_Two(41))
print(is_Sum_Of_Powers_Of_Two(42))
print(is_Sum_Of_Powers_Of_Two(43))
print(is_Sum_Of_Powers_Of_Two(44))
print(is_Sum_Of_Powers_Of_Two(45))
print(is_Sum_Of_Powers_Of_Two(46))
print(is_Sum_Of_Powers_Of_Two(47))
print(is_Sum_Of_Powers_Of_Two(48))
print(is_Sum_Of_Powers_Of_Two(49))
print(is_Sum_Of_Powers_Of_Two(50))
print(is_Sum_Of_Powers_Of_Two(51))
print(is_Sum_Of_Powers_Of_Two(52))
print(is_Sum_Of_Powers_Of_Two(53))
print(is_Sum_Of_Powers_Of_Two(54))
print(is_Sum_Of_Powers_Of_Two(55))
print(is_Sum_Of_Powers_Of_Two(56))
print(is_Sum_Of_Powers_Of_Two(57))
print(is_Sum_Of_Powers_Of_Two(58))
print(is_Sum_Of_Powers_Of_Two(59))
print(is_Sum_Of_Powers_Of_Two(60))
print(