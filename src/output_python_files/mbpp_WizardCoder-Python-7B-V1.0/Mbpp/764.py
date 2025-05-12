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
print(number_ctr('a1b2c3d4e5f6g7h8i9j0')) # Output: 10
print(number_ctr('abcdefghijklmnopqrstuvwxyz')) # Output: 0
print(number_ctr('1234567890')) # Output: 10
print(number_ctr('1a2b3c4d5e6f7g8h9i0j')) # Output: 10
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz')) # Output: 10
print(number_ctr('abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 10
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz')) # Output: 10
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('1234567890abcdefghijklmnopqrstuvwxyz1234567890')) # Output: 20
print(number_ctr('123456789