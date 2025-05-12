"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Diff(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum % 11 == 0

print(is_Diff(12345)) # False
print(is_Diff(1234)) # True
print(is_Diff(12341)) # False
print(is_Diff(12340)) # True
print(is_Diff(123411)) # True
print(is_Diff(123412)) # False
print(is_Diff(123410)) # True
print(is_Diff(1234101)) # False
print(is_Diff(1234100)) # True
print(is_Diff(1234111)) # False
print(is_Diff(12341001)) # True
print(is_Diff(12341000)) # True
print(is_Diff(12341111)) # False
print(is_Diff(123410001)) # True
print(is_Diff(123410000)) # True
print(is_Diff(123411111) # False
print(is_Diff(1234100001) # True
print(is_Diff(1234100000) # True
print(is_Diff(1234567891011) # False
print(is_Diff(1234567891010) # True
print(is_Diff(123456789101) # False
print(is_Diff(123456789100) # True
print(is_Diff(123456789111) # False
print(is_Diff(1234567891000) # True
print(is_Diff(1234567891111) # False
print(is_Diff(12345678910000) # True
print(is_Diff(12345678911111) # False
print(is_Diff(123456789100000) # True
print(is_Diff(123456789111111) # False
print(is_Diff(1234567891000000) # True
print(is_Diff(1234567891111111) # False
print(is_Diff(12345678910000000) # True
print(is_Diff(12345678911111111) # False
print(is_Diff(123456789100000000) # True
print(is_Diff(123456789111111111) # False
print(is_Diff(123456789100000000) # True
print(is_Diff(123456789111111111) # False
print(is_Diff(1234567891000000000) # True
print(is_Diff(1234567891111111111) # False
print(is_Diff(1234567891000000000) # True
print(is_Diff(1234567891111111111)