"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""

def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n //= 2
    while n != 1:
        if n % 2 == 1:
            return False
        n //= 2
    return True

# Test cases
print(is_Sum_Of_Powers_Of_Two(10)) # True
print(is_Sum_Of_Powers_Of_Two(15)) # False
print(is_Sum_Of_Powers_Of_Two(20)) # True
print(is_Sum_Of_Powers_Of_Two(21)) # False
print(is_Sum_Of_Powers_Of_Two(22)) # True
print(is_Sum_Of_Powers_Of_Two(23)) # False
print(is_Sum_Of_Powers_Of_Two(24)) # True
print(is_Sum_Of_Powers_Of_Two(25)) # False
print(is_Sum_Of_Powers_Of_Two(26)) # True
print(is_Sum_Of_Powers_Of_Two(27)) # False
print(is_Sum_Of_Powers_Of_Two(28)) # True
print(is_Sum_Of_Powers_Of_Two(29)) # False
print(is_Sum_Of_Powers_Of_Two(30)) # True
print(is_Sum_Of_Powers_Of_Two(31)) # False
print(is_Sum_Of_Powers_Of_Two(32)) # True
print(is_Sum_Of_Powers_Of_Two(33)) # False
print(is_Sum_Of_Powers_Of_Two(34)) # True
print(is_Sum_Of_Powers_Of_Two(35)) # False
print(is_Sum_Of_Powers_Of_Two(36)) # True
print(is_Sum_Of_Powers_Of_Two(37)) # False
print(is_Sum_Of_Powers_Of_Two(38)) # True
print(is_Sum_Of_Powers_Of_Two(39)) # False
print(is_Sum_Of_Powers_Of_Two(40)) # True
print(is_Sum_Of_Powers_Of_Two(41)) # False
print(is_Sum_Of_Powers_Of_Two(42)) # True
print(is_Sum_Of_Powers_Of_Two(43)) # False
print(is_Sum_Of_Powers_Of_Two(44)) # True
print(is_Sum_Of_Powers_Of_Two(45)) # False
print(is_Sum_Of_Powers_Of_Two(46)) # True
print(is_Sum_Of_Powers_Of_Two(47)) # False
print(is_Sum_Of_Powers_Of_Two(48)) # True
print(is_Sum_Of_Powers_Of_Two(49)) # False
print(is_Sum_Of_Powers_Of_Two(50)) # True
print(is_Sum_Of_Powers_Of_Two(51)) # False
print(is_Sum_Of_Powers_Of_Two(52)) # True
print(is_Sum_Of_Powers_Of_Two(53)) # False
print(is_Sum_Of_Powers_Of_Two(54)) # True
print(is_Sum_Of_Powers_Of_Two(55)) # False
print(is_Sum_Of_Powers_Of_Two(56)) # True
print(is