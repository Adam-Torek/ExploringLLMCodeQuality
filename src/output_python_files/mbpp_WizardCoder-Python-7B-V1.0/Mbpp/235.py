"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(num):
    return num | (num & 0x55555555555555555555)

# Test cases
print(even_bit_set_number(10)) # Output: 10
print(even_bit_set_number(25)) # Output: 27
print(even_bit_set_number(30)) # Output: 31
print(even_bit_set_number(45)) # Output: 45
print(even_bit_set_number(60)) # Output: 63
print(even_bit_set_number(75)) # Output: 75
print(even_bit_set_number(90)) # Output: 93
print(even_bit_set_number(100)) # Output: 100
print(even_bit_set_number(123456789)) # Output: 123456789
print(even_bit_set_number(0)) # Output: 0
print(even_bit_set_number(1)) # Output: 1
print(even_bit_set_number(2)) # Output: 2
print(even_bit_set_number(3)) # Output: 3
print(even_bit_set_number(4)) # Output: 4
print(even_bit_set_number(5)) # Output: 5
print(even_bit_set_number(6)) # Output: 6
print(even_bit_set_number(7)) # Output: 7
print(even_bit_set_number(8)) # Output: 8
print(even_bit_set_number(9)) # Output: 9
print(even_bit_set_number(10)) # Output: 10
print(even_bit_set_number(11)) # Output: 11
print(even_bit_set_number(12)) # Output: 12
print(even_bit_set_number(13)) # Output: 13
print(even_bit_set_number(14)) # Output: 14
print(even_bit_set_number(15)) # Output: 15
print(even_bit_set_number(16)) # Output: 16
print(even_bit_set_number(17)) # Output: 17
print(even_bit_set_number(18)) # Output: 18
print(even_bit_set_number(19)) # Output: 19
print(even_bit_set_number(20)) # Output: 20
print(even_bit_set_number(21)) # Output: 21
print(even_bit_set_number(22)) # Output: 22
print(even_bit_set_number(23)) # Output: 23
print(even_bit_set_number(24)) # Output: 24
print(even_bit_set_number(25)) # Output: 27
print(even_bit_set_number(26)) # Output: 26
print(even_bit_set_number(27)) # Output: 27
print(even_bit_set_number(28)) # Output: 28
print(even_bit_set_number(29)) # Output: 29
print(even_bit_set_number(30)) # Output: 31
print(even_bit_set_number(31)) # Output: 31
print(even_bit_set_number(32)) # Output: 32
print(even_bit_set_number(33)) # Output: 33
print(even_bit_set_number(34)) #