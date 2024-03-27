"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""

def is_Diff(num):
    return num % 11 == 0

assert is_Diff(12345) == False
assert is_Diff(123456) == True
assert is_Diff(1234567) == False
assert is_Diff(12345678) == True
assert is_Diff(123456789) == False
assert is_Diff(1234567890) == True
assert is_Diff(12345678901) == False
assert is_Diff(123456789012) == True
assert is_Diff(1234567890123) == False
assert is_Diff(12345678901234) == True
assert is_Diff(123456789012345) == False
assert is_Diff(1234567890123456) == True
assert is_Diff(12345678901234567) == False
assert is_Diff(123456789012345678) == True
assert is_Diff(1234567890123456789) == False
assert is_Diff(12345678901234567890) == True
assert is_Diff(123456789012345678901) == False
assert is_Diff(1234567890123456789012) == True
assert is_Diff(12345678901234567890123) == False
assert is_Diff(123456789012345678901234) == True
assert is_Diff(1234567890123456789012345) == False
assert is_Diff(12345678901234567890123456) == True
assert is_Diff(123456789012345678901234567) == False
assert is_Diff(1234567890123456789012345678) == True
assert is_Diff(12345678901234567890123456789) == False
assert is_Diff(123456789012345678901234567890) == True
assert is_Diff(1234567890123456789012345678901) == False
assert is_Diff(12345678901234567890123456789012) == True
assert is_Diff(123456789012345678901234567890123) == False
assert is_Diff(1234567890123456789012345678901234) == True
assert is_Diff(12345678901234567890123456789012345) == False
assert is_Diff(123456789012345678901234567890123456) == True
assert is_Diff(1234567890123456789