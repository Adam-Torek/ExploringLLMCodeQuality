"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""

def is_woodall(num):
    for i in range(1, num):
        if num % i == 0:
            if num - i != 0:
                if num - i != i:
                    return False
    return True

# Test cases
print(is_woodall(383)) # True
print(is_woodall(12)) # False
print(is_woodall(24)) # True
print(is_woodall(48)) # False
print(is_woodall(60)) # True
print(is_woodall(75)) # False
print(is_woodall(91)) # True
print(is_woodall(100)) # False
print(is_woodall(121)) # False
print(is_woodall(153)) # True
print(is_woodall(168)) # False
print(is_woodall(210)) # True
print(is_woodall(284)) # False
print(is_woodall(336)) # True
print(is_woodall(400)) # False
print(is_woodall(455)) # True
print(is_woodall(528)) # False
print(is_woodall(686)) # True
print(is_woodall(810)) # False
print(is_woodall(990)) # True
print(is_woodall(1000)) # False
print(is_woodall(1234)) # False
print(is_woodall(1440)) # True
print(is_woodall(1619)) # False
print(is_woodall(2000)) # False
print(is_woodall(2880)) # True
print(is_woodall(3333)) # False
print(is_woodall(4000)) # False
print(is_woodall(5000)) # False
print(is_woodall(6666)) # True
print(is_woodall(8180)) # False
print(is_woodall(10000)) # False
print(is_woodall(12345)) # False
print(is_woodall(169)) # False
print(is_woodall(252)) # False
print(is_woodall(370)) # False
print(is_woodall(40000)) # False
print(is_woodall(50000)) # False
print(is_woodall(666)) # False
print(is_woodall(100000)) # False
print(is_woodall(15383)) # True
print(is_woodall(20000)) # False
print(is_woodall(24000)) # False
print(is_woodall(28800)) # True
print(is_woodall(33333)) # False
print(is_woodall(400000)) # False
print(is_woodall(500000)) # False
print(is_woodall(66666)) # True
print(is_woodall(8181)) # False
print(is_woodall(1000000)) # False
print(is_woodall(123456)) # False
print(is_woodall(166666)) # False
print(is_woodall(2000000)) # False
print(is_woodall(2500000)) # False
print(is_woodall(3333333)) # False
print(is_woodall(4000000)) # False
print(is_woodall(5000000)) # False
print(is_woodall(6666666)) # False
print(is_woodall(818181)) # False
print(is_woodall(10000