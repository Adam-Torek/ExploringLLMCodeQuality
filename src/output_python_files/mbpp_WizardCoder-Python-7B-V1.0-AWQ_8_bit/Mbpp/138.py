"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""

def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    power = 0
    while 2**power <= n:
        power += 1
    return n == 2**(power-1)

print(is_Sum_Of_Powers_Of_Two(10)) # True
print(is_Sum_Of_Powers_Of_Two(15)) # False
print(is_Sum_Of_Powers_Of_Two(20)) # True
print(is_Sum_Of_Powers_Of_Two(21)) # False
print(is_Sum_Of_Powers_Of_Two(30)) # True
print(is_Sum_Of_Powers_Of_Two(31)) # False
print(is_Sum_Of_Powers_Of_Two(40)) # True
print(is_Sum_Of_Powers_Of_Two(45)) # False
print(is_Sum_Of_Powers_Of_Two(50)) # True
print(is_Sum_Of_Powers_Of_Two(51)) # False
print(is_Sum_Of_Powers_Of_Two(60)) # True
print(is_Sum_Of_Powers_Of_Two(63)) # False
print(is_Sum_Of_Powers_Of_Two(70)) # True
print(is_Sum_Of_Powers_Of_Two(71)) # False
print(is_Sum_Of_Powers_Of_Two(80)) # True
print(is_Sum_Of_Powers_Of_Two(81)) # False
print(is_Sum_Of_Powers_Of_Two(90)) # True
print(is_Sum_Of_Powers_Of_Two(91)) # False
print(is_Sum_Of_Powers_Of_Two(100)) # True
print(is_Sum_Of_Powers_Of_Two(101)) # False
print(is_Sum_Of_Powers_Of_Two(128)) # True
print(is_Sum_Of_Powers_Of_Two(129)) # False
print(is_Sum_Of_Powers_Of_Two(150)) # True
print(is_Sum_Of_Powers_Of_Two(151)) # False
print(is_Sum_Of_Powers_Of_Two(160)) # True
print(is_Sum_Of_Powers_Of_Two(161)) # False
print(is_Sum_Of_Powers_Of_Two(170)) # True
print(is_Sum_Of_Powers_Of_Two(171)) # False
print(is_Sum_Of_Powers_Of_Two(180)) # True
print(is_Sum_Of_Powers_Of_Two(181)) # False
print(is_Sum_Of_Powers_Of_Two(190)) # True
print(is_Sum_Of_Powers_Of_Two(191)) # False
print(is_Sum_Of_Powers_Of_Two(200)) # True
print(is_Sum_Of_Powers_Of_Two(201)) # False
print(is_Sum_Of_Powers_Of_Two(255)) # True
print(is_Sum_Of_Powers_Of_Two(256)) # False
print(is_Sum_Of_Powers_Of_Two(257)) # False
print(is_Sum_Of_Powers_Of_Two(258)) # True
print(is_Sum_Of_Powers_Of_Two(259)) # False
print(is_Sum_Of_Powers_Of_Two(260)) # True
print