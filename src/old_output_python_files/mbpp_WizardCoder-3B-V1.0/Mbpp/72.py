"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""

def dif_Square(num):
    if num < 0:
        return False
    for i in range(1, int(num**0.5)+1):
        if num % i == 0 and num // i == i:
            return True
    return False

# Test cases
print(dif_Square(5)) # True
print(dif_Square(16)) # True
print(dif_Square(25)) # False
print(dif_Square(0)) # False<|endoftext|>