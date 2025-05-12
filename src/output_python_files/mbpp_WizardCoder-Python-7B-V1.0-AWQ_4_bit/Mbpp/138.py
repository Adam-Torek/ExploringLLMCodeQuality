"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""

def is_Sum_Of_Powers_Of_Two(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 == 1:
        return False
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            return False
    return True

# Test cases
print(is_Sum_Of_Powers_Of_Two(10)) # True
print(is_Sum_Of_Powers_Of_Two(15)) # False
print(is_Sum_Of_Powers_Of_Two(20)) # True
print(is_Sum_Of_Powers_Of_Two(21)) # False
print(is_Sum_Of_Powers_Of_Two(30)) # True
print(is_Sum_Of_Powers_Of_Two(31)) # False
print(is_Sum_Of_Powers_Of_Two(40)) # True
print(is_Sum_Of_Powers_Of_Two(41)) # False
print(is_Sum_Of_Powers_Of_Two(50)) # True
print(is_Sum_Of_Powers_Of_Two(51)) # False
print(is_Sum_Of_Powers_Of_Two(60)) # True
print(is_Sum_Of_Powers_Of_Two(61)) # False
print(is_Sum_Of_Powers_Of_Two(70)) # True
print(is_Sum_Of_Powers_Of_Two(71)) # False
print(is_Sum_Of_Powers_Of_Two(80)) # True
print(is_Sum_Of_Powers_Of_Two(81)) # False
print(is_Sum_Of_Powers_Of_Two(90)) # True
print(is_Sum_Of_Powers_Of_Two(91)) # False
print(is_Sum_Of_Powers_Of_Two(100)) # True
print(is_Sum_Of_Powers_Of_Two(101)) # False
print(is_Sum_Of_Powers_Of_Two(102)) # False
print(is_Sum_Of_Powers_Of_Two(103)) # False
print(is_Sum_Of_Powers_Of_Two(104)) # True
print(is_Sum_Of_Powers_Of_Two(105)) # False
print(is_Sum_Of_Powers_Of_Two(106)) # False
print(is_Sum_Of_Powers_Of_Two(107)) # False
print(is_Sum_Of_Powers_Of_Two(108)) # True
print(is_Sum_Of_Powers_Of_Two(109)) # False
print(is_Sum_Of_Powers_Of_Two(110)) # True
print(is_Sum_Of_Powers_Of_Two(111)) # False
print(is_Sum_Of_Powers_Of_Two(112)) # False
print(is_Sum_Of_Powers_Of_Two(113)) # False
print(is_Sum_Of_Powers_Of_Two(114)) # True
print(is_Sum_Of_Powers_Of_Two(115)) # False
print(is_Sum_Of_Powers_Of_Two(116)) # True
print(is_Sum_Of_Powers_Of_Two(117)) # False
print(is_Sum_Of_Powers_Of_Two(118)) # False
print(is_Sum_Of_Pow