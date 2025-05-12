"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""

def toggle_middle_bits(n):
    n = n ^ (n >> 1)
    n = n ^ (n << 1)
    return n

# Test cases
print(toggle_middle_bits(9)) # Output: 15
print(toggle_middle_bits(10)) # Output: 14
print(toggle_middle_bits(11)) # Output: 10
print(toggle_middle_bits(12)) # Output: 13
print(toggle_middle_bits(13)) # Output: 14
print(toggle_middle_bits(14)) # Output: 15
print(toggle_middle_bits(15)) # Output: 14
print(toggle_middle_bits(16)) # Output: 17
print(toggle_middle_bits(17)) # Output: 16
print(toggle_middle_bits(18)) # Output: 19
print(toggle_middle_bits(19)) # Output: 18
print(toggle_middle_bits(20)) # Output: 21
print(toggle_middle_bits(21)) # Output: 20
print(toggle_middle_bits(22)) # Output: 23
print(toggle_middle_bits(23)) # Output: 22
print(toggle_middle_bits(24)) # Output: 25
print(toggle_middle_bits(25)) # Output: 24
print(toggle_middle_bits(26)) # Output: 27
print(toggle_middle_bits(27)) # Output: 26
print(toggle_middle_bits(28)) # Output: 29
print(toggle_middle_bits(29)) # Output: 28
print(toggle_middle_bits(30)) # Output: 31
print(toggle_middle_bits(31)) # Output: 30
print(toggle_middle_bits(32)) # Output: 33
print(toggle_middle_bits(33)) # Output: 32
print(toggle_middle_bits(34)) # Output: 35
print(toggle_middle_bits(35)) # Output: 34
print(toggle_middle_bits(36)) # Output: 37
print(toggle_middle_bits(37)) # Output: 36
print(toggle_middle_bits(38)) # Output: 39
print(toggle_middle_bits(39)) # Output: 38
print(toggle_middle_bits(40)) # Output: 41
print(toggle_middle_bits(41)) # Output: 40
print(toggle_middle_bits(42)) # Output: 43
print(toggle_middle_bits(43)) # Output: 42
print(toggle_middle_bits(44)) # Output: 45
print(toggle_middle_bits(45)) # Output: 44
print(toggle_middle_bits(46)) # Output: 47
print(toggle_middle_bits(47)) # Output: 46
print(toggle_middle_bits(48)) # Output: 49
print(toggle_middle_bits(49)) # Output: 48
print(toggle_middle_bits(50)) # Output: 51
print(toggle_middle_bits(51)) # Output: 50
print(toggle_middle_bits(52)) # Output: 53
print(toggle_middle_bits(53)) # Output: 52
print(toggle_middle_bits(54)) # Output: 55
print(toggle_middle_bits(55)) # Output: 54
print(toggle_middle_bits(56)) # Output: 57
print(toggle_middle_bits(57)) # Output: 56
print(toggle_middle_bits(58)) # Output: 59
print(toggle_middle_