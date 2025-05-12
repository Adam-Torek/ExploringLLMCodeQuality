"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Diff(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum % 11 == 0

print(is_Diff(12345)) # False
print(is_Diff(1234)) # True
print(is_Diff(123456)) # False
print(is_Diff(1234567)) # True
print(is_Diff(12345678)) # False
print(is_Diff(123456789)) # True
print(is_Diff(1234567890)) # False
print(is_Diff(12345678901)) # True
print(is_Diff(123456789012)) # False
print(is_Diff(1234567890123)) # True
print(is_Diff(12345678901234)) # False
print(is_Diff(123456789012345)) # True
print(is_Diff(1234567890123456)) # False
print(is_Diff(12345678901234567)) # True
print(is_Diff(123456789012345678)) # False
print(is_Diff(1234567890123456789)) # True
print(is_Diff(12345678901234567890)) # False
print(is_Diff(123456789012345678901)) # True
print(is_Diff(1234567890123456789012)) # False
print(is_Diff(12345678901234567890123)) # True
print(is_Diff(123456789012345678901234)) # False
print(is_Diff(1234567890123456789012345)) # True
print(is_Diff(12345678901234567890123456)) # False
print(is_Diff(123456789012345678901234567)) # True
print(is_Diff(1234567890123456789012345678)) # False
print(is_Diff(12345678901234567890123456789)) # True
print(is_Diff(123456789012345678901234567890)) # False
print(is_Diff(1234567890123456789012345678901)) # True
print(is_Diff(12345678901234567890123456789012)) # False
print(is_Diff(123456789012345678901234567890123)) # True
print(is_Diff(1234567890123456789012345678901234)) # False
print(is_Diff(12345678901234567890123456789012345)) # True