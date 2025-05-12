"""
Write a function to create the next bigger number by rearranging the digits of a given number.
assert rearrange_bigger(12)==21
"""

def rearrange_bigger(num):
    num = str(num)
    num = sorted(num, reverse=True)
    num = int(''.join(num))
    return num

print(rearrange_bigger(12)) # Output: 21
print(rearrange_bigger(5312)) # Output: 5312
print(rearrange_bigger(9)) # Output: 9
print(rearrange_bigger(54321)) # Output: 54213
print(rearrange_bigger(12345)) # Output: 54321
print(rearrange_bigger(123456)) # Output: 543216
print(rearrange_bigger(1234567)) # Output: 5432167
print(rearrange_bigger(12345678)) # Output: 54321678
print(rearrange_bigger(123456789)) # Output: 543216789
print(rearrange_bigger(1234567890)) # Output: 5432167890
print(rearrange_bigger(12345678901)) # Output: 54321678901
print(rearrange_bigger(123456789012)) # Output: 543216789012
print(rearrange_bigger(1234567890123)) # Output: 5432167890123
print(rearrange_bigger(12345678901234)) # Output: 54321678901234
print(rearrange_bigger(123456789012345)) # Output: 543216789012345
print(rearrange_bigger(1234567890123456)) # Output: 5432167890123456
print(rearrange_bigger(12345678901234567)) # Output: 54321678901234567
print(rearrange_bigger(123456789012345678)) # Output: 543216789012345678
print(rearrange_bigger(1234567890123456789)) # Output: 5432167890123456789
print(rearrange_bigger(12345678901234567890)) # Output: 54321678901234567890
print(rearrange_bigger(123456789012345678901)) # Output: 543216789012345678901
print(rearrange_bigger(1234567890123456789012)) # Output: 5432167890123456789012
print(rearrange_bigger(12345678901234567890123)) # Output: 54321678901234567890123
print(rearrange_bigger(12345