"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""

def is_undulating(n):
    if n < 10:
        return False
    if n % 10 == 0:
        return True
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_undulating(1212121)) # True
print(is_undulating(123456789)) # False
print(is_undulating(12345678)) # True
print(is_undulating(1234567)) # False
print(is_undulating(123456)) # True
print(is_undulating(12345)) # False
print(is_undulating(1234)) # True
print(is_undulating(123)) # False
print(is_undulating(12)) # True
print(is_undulating(1)) # False<|endoftext|>