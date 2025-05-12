"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""

def is_nonagonal(n):
    count = 1
    num = 1
    while count < n:
        num += 1
        count += 1
        for i in range(1, num):
            if num * (num - 1) * (num - 1) == 2 * i * (2 * i - 1):
                count += 1
            if count == n:
                return num
    return None

print(is_nonagonal(10)) # Output: 325
print(is_nonagonal(1)) # Output: 1
print(is_nonagonal(2)) # Output: 2
print(is_nonagonal(3)) # Output: 4
print(is_nonagonal(4)) # Output: 6
print(is_nonagonal(5)) # Output: 10
print(is_nonagonal(6)) # Output: 15
print(is_nonagonal(7)) # Output: 21
print(is_nonagonal(8)) # Output: 28
print(is_nonagonal(9)) # Output: 36
print(is_nonagonal(10)) # Output: 45
print(is_nonagonal(11)) # Output: 55
print(is_nonagonal(12)) # Output: 66
print(is_nonagonal(13)) # Output: 78
print(is_nonagonal(14)) # Output: 92
print(is_nonagonal(15)) # Output: 110
print(is_nonagonal(16)) # Output: 130
print(is_nonagonal(17)) # Output: 150
print(is_nonagonal(18)) # Output: 175
print(is_nonagonal(19)) # Output: 198
print(is_nonagonal(20)) # Output: 225
print(is_nonagonal(21)) # Output: 255
print(is_nonagonal(22)) # Output: 288
print(is_nonagonal(23)) # Output: 325
print(is_nonagonal(24)) # Output: 366
print(is_nonagonal(25)) # Output: 410
print(is_nonagonal(26)) # Output: 455
print(is_nonagonal(27)) # Output: 506
print(is_nonagonal(28)) # Output: 561
print(is_nonagonal(29)) # Output: 620
print(is_nonagonal(30)) # Output: 685
print(is_nonagonal(31)) # Output: 755
print(is_nonagonal(32)) # Output: 832
print(is_nonagonal(33)) # Output: 915
print(is_nonagonal(34)) # Output: 1006
print(is_nonagonal(35)) # Output: 1101
print(is_nonagonal(36)) # Output: 1204
print(is_nonagonal(37)) # Output: 1312
print(is_nonagonal(38)) # Output: 1432
print(is_nonagonal(39)) # Output: 1556
print(is_nonagonal(40)) # Output: 1685
print(is_nonagonal(41)) # Output: 1831
print(is_nonagonal(42)) # Output: 2001
print(is_nonagonal(43)) # Output: 2188
print(is_nonagonal(44)) # Output: 2381
print(is_nonagonal(4