"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
def dif_Square(n):
    for i in range(1, int(n/2)+1):
        for j in range(1, int(n/2)+1):
            if i*i + j*j == n:
                return True
    return False

# Test cases
print(dif_Square(5)) # True
print(dif_Square(13)) # True
print(dif_Square(10)) # False
print(dif_Square(17)) # True
print(dif_Square(25)) # True
print(dif_Square(30)) # False
print(dif_Square(37)) # True
print(dif_Square(40)) # True
print(dif_Square(41)) # False
print(dif_Square(42)) # True
print(dif_Square(43)) # False
print(dif_Square(44)) # True
print(dif_Square(45)) # False
print(dif_Square(46)) # True
print(dif_Square(47)) # False
print(dif_Square(48)) # True
print(dif_Square(49)) # False
print(dif_Square(50)) # True
print(dif_Square(51)) # False
print(dif_Square(52)) # True
print(dif_Square(53)) # False
print(dif_Square(54)) # True
print(dif_Square(55)) # False
print(dif_Square(56)) # True
print(dif_Square(57)) # False
print(dif_Square(58)) # True
print(dif_Square(59)) # False
print(dif_Square(60)) # True
print(dif_Square(61)) # False
print(dif_Square(62)) # True
print(dif_Square(63)) # False
print(dif_Square(64)) # True
print(dif_Square(65)) # False
print(dif_Square(66)) # True
print(dif_Square(67)) # False
print(dif_Square(68)) # True
print(dif_Square(69)) # False
print(dif_Square(70)) # True
print(dif_Square(71)) # False
print(dif_Square(72)) # True
print(dif_Square(73)) # False
print(dif_Square(74)) # True
print(dif_Square(75)) # False
print(dif_Square(76)) # True
print(dif_Square(77)) # False
print(dif_Square(78)) # True
print(dif_Square(79)) # False
print(dif_Square(80)) # True
print(dif_Square(81)) # False
print(dif_Square(82)) # True
print(dif_Square(83)) # False
print(dif_Square(84)) # True
print(dif_Square(85)) # False
print(dif_Square(86)) # True
print(dif_Square(87)) # False
print(dif_Square(88)) # True
print(dif_Square(89)) # False
print(dif_Square(90)) # True
print(dif_Square(91)) # False
print(dif_Square(92)) # True
print(dif_Square(93)) # False
print(dif_Square(94)) # True
print(dif_Square(95)) # False
print(dif_Square(96)) # True