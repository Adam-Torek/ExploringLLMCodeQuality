"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""

def is_perfect_square(n: int) -> bool:
    if n == 1:
        return True
    i = 1
    while i * i <= n:
        i += 1
    return i * i == n

# Test cases
print(is_perfect_square(16)) # True
print(is_perfect_square(10)) # False
print(is_perfect_square(25)) # True
print(is_perfect_square(1)) # True
print(is_perfect_square(0)) # True
print(is_perfect_square(100)) # False
print(is_perfect_square(101)) # False
print(is_perfect_square(4)) # True
print(is_perfect_square(9)) # True
print(is_perfect_square(2)) # True
print(is_perfect_square(3)) # False
print(is_perfect_square(5)) # False
print(is_perfect_square(6)) # True
print(is_perfect_square(7)) # False
print(is_perfect_square(8)) # True
print(is_perfect_square(9)) # True
print(is_perfect_square(10)) # False
print(is_perfect_square(11)) # False
print(is_perfect_square(12)) # True
print(is_perfect_square(13)) # False
print(is_perfect_square(14)) # False
print(is_perfect_square(15)) # True
print(is_perfect_square(16)) # True
print(is_perfect_square(17)) # False
print(is_perfect_square(18)) # False
print(is_perfect_square(19)) # False
print(is_perfect_square(20)) # True
print(is_perfect_square(21)) # False
print(is_perfect_square(22)) # False
print(is_perfect_square(23)) # False
print(is_perfect_square(24)) # True
print(is_perfect_square(25)) # True
print(is_perfect_square(26)) # False
print(is_perfect_square(27)) # False
print(is_perfect_square(28)) # True
print(is_perfect_square(29)) # False
print(is_perfect_square(30)) # False
print(is_perfect_square(31)) # False
print(is_perfect_square(32)) # True
print(is_perfect_square(33)) # False
print(is_perfect_square(34)) # False
print(is_perfect_square(35)) # False
print(is_perfect_square(36)) # True
print(is_perfect_square(37)) # False
print(is_perfect_square(38)) # False
print(is_perfect_square(39)) # False
print(is_perfect_square(40)) # True
print(is_perfect_square(41)) # False
print(is_perfect_square(42)) # False
print(is_perfect_square(43)) # False
print(is_perfect_square(44)) # True
print(is_perfect_square(45)) # False
print(is_perfect_square(46)) # False
print(is_perfect_square(47)) # False
print(is_perfect_square(48)) # True
print(is_perfect_square(49)) # False
print(is_perfect_square(50)) # True
print(is_perfect_square(51)) # False
print(is_perfect_square(52)) # False
print(is_perfect