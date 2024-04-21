"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""

def is_Sum_Of_Powers_Of_Two(num):
    if num == 0:
        return True
    if num % 2 == 0:
        return False
    if num % 4 == 0:
        return False
    if num % 8 == 0:
        return False
    if num % 16 == 0:
        return False
    if num % 32 == 0:
        return False
    if num % 64 == 0:
        return False
    if num % 128 == 0:
        return False
    if num % 256 == 0:
        return False
    if num % 512 == 0:
        return False
    if num % 1024 == 0:
        return False
    if num % 2048 == 0:
        return False
    if num % 4096 == 0:
        return False
    if num % 8192 == 0:
        return False
    if num % 16384 == 0:
        return False
    if num % 32768 == 0:
        return False
    if num % 65536 == 0:
        return False
    if num % 131072 == 0:
        return False
    if num % 262144 == 0:
        return False
    if num % 524288 == 0:
        return False
    if num % 1048576 == 0:
        return False
    if num % 2097152 == 0:
        return False
    if num % 4194304 == 0:
        return False
    if num % 8388608 == 0:
        return False
    if num % 16777216 == 0:
        return False
    if num % 33554432 == 0:
        return False
    if num % 67108864 == 0:
        return False
    if num % 134217728 == 0:
        return False
    if num % 268435456 == 0:
        return False
    if num % 536870912 == 0:
        return False
    if num % 1073741824 == 0:
        return False
    if num % 2147483648 == 0:
        return False
    return True

# Test cases
print(is_Sum_Of_Powers_Of_Two(10)) # True
print(is_Sum_Of_Powers_Of_Two(12)) # False
print(is_Sum_Of_Powers_Of_Two(16)) # True
print(is_Sum_Of_Powers_Of_Two(32)) # False
print(is_Sum_Of_Powers_Of_Two(64)) # True
print(is_Sum_Of_Powers_Of_Two(128)) # False
print(is_Sum_Of_Powers_Of_Two(256)) # True
print(is_Sum_Of_Powers_Of_Two(512)) # False
print(is_Sum_Of_Powers_Of_Two(1024)) # True
print(is_Sum_Of_Powers_Of_Two(2048)) # False
print(is_Sum_Of_Powers_Of_Two(4096)) # True
print(is_Sum_Of_Powers_Of_Two(8192)) # False
print(is_Sum_Of_Powers_Of_Two(16384)) # True
print(is_Sum_Of_Powers_Of_Two(32768)) # False
print(is_Sum_Of_Powers_Of_Two(65536)) # True
print(is_Sum_Of_Powers_Of_Two(131072)) # False
print(is_Sum_Of_Powers_Of_Two(262144)) # True
print(is_Sum_Of_Powers_Of_Two