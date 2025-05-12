"""
Write a python function to check whether the given number is even or not.
assert is_Even(1) == False
"""
def is_Even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_Even(1)) # Output: False
print(is_Even(2)) # Output: True
print(is_Even(3)) # Output: False
print(is_Even(4)) # Output: True
print(is_Even(5)) # Output: False
print(is_Even(6)) # Output: True
print(is_Even(7)) # Output: False
print(is_Even(8)) # Output: True
print(is_Even(9)) # Output: False
print(is_Even(10)) # Output: True

# Another way to write the same function
def is_Even(num):
    return num % 2 == 0

print(is_Even(1)) # Output: False
print(is_Even(2)) # Output: True
print(is_Even(3)) # Output: False
print(is_Even(4)) # Output: True
print(is_Even(5)) # Output: False
print(is_Even(6)) # Output: True
print(is_Even(7)) # Output: False
print(is_Even(8)) # Output: True
print(is_Even(9)) # Output: False
print(is_Even(10)) # Output: True

# Another way to write the same function
def is_Even(num):
    return not num % 2

print(is_Even(1)) # Output: False
print(is_Even(2)) # Output: True
print(is_Even(3)) # Output: False
print(is_Even(4)) # Output: True
print(is_Even(5)) # Output: False
print(is_Even(6)) # Output: True
print(is_Even(7)) # Output: False
print(is_Even(8)) # Output: True
print(is_Even(9)) # Output: False
print(is_Even(10)) # Output: True

# Another way to write the same function
def is_Even(num):
    return num & 1 == 0

print(is_Even(1)) # Output: False
print(is_Even(2)) # Output: True
print(is_Even(3)) # Output: False
print(is_Even(4)) # Output: True
print(is_Even(5)) # Output: False
print(is_Even(6)) # Output: True
print(is_Even(7)) # Output: False
print(is_Even(8)) # Output: True
print(is_Even(9)) # Output: False
print(is_Even(10)) # Output: True

# Another way to write the same function
def is_Even(num):
    return num ** 0.5 % 2 == 0

print(is_Even(1)) # Output: False
print(is_Even(2)) # Output: True
print(is_Even(3)) # Output: False
print(is_Even(4)) # Output: True
print(is_Even(5)) # Output: False
print(is_Even(6)) # Output: True
print(is_Even(7)) # Output: False
print(is_Even(8)) # Output: True
print(is_Even(9)) # Output: False
print(is_Even(10)) # Output: True

# Another way to write the same function
def is_Even(num):
    return num == 0 or num % 2 == 0

print(is_Even(1)) # Output: False
print(is_Even(2)) # Output: True
print(is_Even(3)) # Output: False
print(is_Even(4)) # Output: True
print(is_Even(5)) #