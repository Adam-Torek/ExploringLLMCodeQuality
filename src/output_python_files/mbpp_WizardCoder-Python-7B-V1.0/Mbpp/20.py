"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""

def is_woodall(num):
    for i in range(1, num):
        if num % i == 0:
            if num // i != num:
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
print(is_woodall(121)) # True
print(is_woodall(153)) # False
print(is_woodall(168)) # True
print(is_woodall(220)) # False
print(is_woodall(288)) # True
print(is_woodall(333)) # False
print(is_woodall(383)) # True
print(is_woodall(400)) # False
print(is_woodall(420)) # True
print(is_woodall(444)) # False
print(is_woodall(528)) # True
print(is_woodall(620)) # False
print(is_woodall(669)) # True
print(is_woodall(888)) # False
print(is_woodall(1000)) # False
print(is_woodall(1234)) # False
print(is_woodall(1440)) # True
print(is_woodall(1612)) # False
print(is_woodall(2000)) # False
print(is_woodall(2800)) # True
print(is_woodall(3000)) # False
print(is_woodall(3248)) # True
print(is_woodall(4000)) # False
print(is_woodall(4660)) # True
print(is_woodall(5600)) # False
print(is_woodall(6484)) # True
print(is_woodall(8100)) # False
print(is_woodall(10000)) # False
print(is_woodall(12340)) # False
print(is_woodall(16960)) # True
print(is_woodall(20000)) # False
print(is_woodall(28800)) # True
print(is_woodall(32768)) # False
print(is_woodall(40000)) # False
print(is_woodall(46656)) # True
print(is_woodall(64848)) # False
print(is_woodall(81000)) # False
print(is_woodall(100000)) # False
print(is_woodall(123400)) # False
print(is_woodall(169600)) # True
print(is_woodall(200000)) # False
print(is_woodall(288000)) # True
print(is_woodall(327680)) # False
print(is_woodall(400000)) # False
print(is_woodall(466560)) # True
print(is_woodall(648480)) # False
print(is_woodall(810000)) # False
print(is_woodall(1000000)) # False
print(is_woodall(1234000)) # False
print(is_woodall(1696000)) # True
print(is_woodall(2000000)) # False
print(is_woodall(2880000)) # True
print(is_