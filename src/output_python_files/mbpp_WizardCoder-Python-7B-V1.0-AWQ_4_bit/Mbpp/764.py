"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""

def number_ctr(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count

print(number_ctr('program2bedone')) # Output: 1
print(number_ctr('hello123world456')) # Output: 6
print(number_ctr('python3.6')) # Output: 3
print(number_ctr('12345')) # Output: 5
print(number_ctr('')) # Output: 0
print(number_ctr('a')) # Output: 0
print(number_ctr('123456')) # Output: 6
print(number_ctr('1a2b3c4d5e6f')) # Output: 6
print(number_ctr('1234567890')) # Output: 10
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz')) # Output: 0
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 10
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz12345678901234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz123456789012345678901234567890')) # Output: 40
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890123456789012345678901234567890')) # Output: 60
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz12345678901234567890123456789012345678901234567890')) # Output: 80
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890123456789012345678901234567890123456789012345678901234567890')) # Output: 120
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')) # Output: 160
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890123456789012345678901234567890123456789012345678901234567890123456789