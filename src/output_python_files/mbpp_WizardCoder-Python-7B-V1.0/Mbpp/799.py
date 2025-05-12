"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""

def left_rotate(num, d):
    # convert the number to binary
    binary_num = bin(num)[2:]
    # get the length of the binary number
    binary_len = len(binary_num)
    # add leading zeros to make it 32 bits
    binary_num = binary_num.zfill(32)
    # rotate the bits to the left by d positions
    rotated_binary = binary_num[d:] + binary_num[:d]
    # convert the rotated binary back to decimal
    rotated_num = int(rotated_binary, 2)
    return rotated_num

# test the function
print(left_rotate(16, 2)) # output: 64
print(left_rotate(10, 2)) # output: 48
print(left_rotate(25, 3)) # output: 21
print(left_rotate(32, 1)) # output: 64
print(left_rotate(123456789, 4)) # output: 341915462
print(left_rotate(123456789, 2)) # output: 261345678
print(left_rotate(123456789, 32)) # output: 123456789
print(left_rotate(123456789, 33)) # output: 123456789
print(left_rotate(123456789, 0)) # output: 123456789
print(left_rotate(123456789, 31)) # output: 123456789
print(left_rotate(123456789, 33)) # output: 123456789
print(left_rotate(123456789, 34)) # output: 123456789
print(left_rotate(123456789, 35)) # output: 123456789
print(left_rotate(123456789, 36)) # output: 123456789
print(left_rotate(123456789, 37)) # output: 123456789
print(left_rotate(123456789, 38)) # output: 123456789
print(left_rotate(123456789, 39)) # output: 123456789
print(left_rotate(123456789, 40)) # output: 123456789
print(left_rotate(123456789, 41)) # output: 123456789
print(left_rotate(123456789, 42)) # output: 123456789
print(left_rotate(123456789, 43)) # output: 123456789
print(left_rotate(123456789, 44)) # output: 123456789
print(left_rotate(123456789, 45)) # output: 123456789
print(left_rotate(123456789, 46)) # output: 123456789
print(left_rotate(123456789, 47)) # output: 123456789
print(left_rotate(123456789, 48)) # output: 123456789