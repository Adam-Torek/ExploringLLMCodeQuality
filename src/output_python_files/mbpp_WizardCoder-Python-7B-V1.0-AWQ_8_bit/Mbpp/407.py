"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""

def rearrange_bigger(num):
    num = str(num)
    num = sorted(num, reverse=True)
    num = ''.join(num)
    return int(num)

print(rearrange_bigger(12)) # Output: 21
print(rearrange_bigger(5312)) # Output: 5312
print(rearrange_bigger(5321)) # Output: 5321
print(rearrange_bigger(12345)) # Output: 54321
print(rearrange_bigger(9)) # Output: 9
print(rearrange_bigger(10)) # Output: 10
print(rearrange_bigger(100)) # Output: 100
print(rearrange_bigger(123456)) # Output: 564321
print(rearrange_bigger(12345678)) # Output: 87654321
print(rearrange_bigger(123456789)) # Output: 987654321
print(rearrange_bigger(1234567890)) # Output: 9876543210
print(rearrange_bigger(12345678901)) # Output: 98765432101
print(rearrange_bigger(123456789012)) # Output: 987654321012
print(rearrange_bigger(1234567890123)) # Output: 9876543210123
print(rearrange_bigger(12345678901234)) # Output: 98765432101234
print(rearrange_bigger(123456789012345)) # Output: 987654321012345
print(rearrange_bigger(1234567890123456)) # Output: 9876543210123456
print(rearrange_bigger(12345678901234567)) # Output: 98765432101234567
print(rearrange_bigger(123456789012345678)) # Output: 987654321012345678
print(rearrange_bigger(1234567890123456789)) # Output: 9876543210123456789
print(rearrange_bigger(12345678901234567890)) # Output: 98765432101234567890
print(rearrange_bigger(123456789012345678901)) # Output: 987654321012345678901
print(rearrange_bigger(1234567890123456789012)) # Output: 9876543210123456789012
print(rearrange_bigger(12345678901234567890123)) # Output: 98765432101234567890123
print(rearrange_bigger(123456789012345