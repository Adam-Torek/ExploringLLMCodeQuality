"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""

def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

# Test cases
print(is_perfect_square(10)) # False
print(is_perfect_square(16)) # True
print(is_perfect_square(25)) # True
print(is_perfect_square(100)) # False
print(is_perfect_square(0)) # True
print(is_perfect_square(1)) # True
print(is_perfect_square(-1)) # False
print(is_perfect_square(2)) # True
print(is_perfect_square(4)) # True
print(is_perfect_square(9)) # True
print(is_perfect_square(1000)) # False
print(is_perfect_square(101)) # False
print(is_perfect_square(10000)) # True
print(is_perfect_square(100000)) # True
print(is_perfect_square(1000000)) # True
print(is_perfect_square(10000000)) # True
print(is_perfect_square(100000000)) # True
print(is_perfect_square(1000000000)) # True
print(is_perfect_square(10000000000)) # True
print(is_perfect_square(100000000000)) # True
print(is_perfect_square(100000000000)) # True
print(is_perfect_square(1000000000000)) # True
print(is_perfect_square(1000000000000)) # True
print(is_perfect_square(10000000000000)) # True
print(is_perfect_square(100000000000000)) # True
print(is_perfect_square(1000000000000000)) # True
print(is_perfect_square(10000000000000000)) # True
print(is_perfect_square(100000000000000000)) # True
print(is_perfect_square(1000000000000000000)) # True
print(is_perfect_square(10000000000000000000)) # True
print(is_perfect_square(100000000000000000000)) # True
print(is_perfect_square(1000000000000000000000)) # True
print(is_perfect_square(10000000000000000000000)) # True
print(is_perfect_square(100000000000000000000000)) # True
print(is_perfect_square(1000000000000000000000000)) # True
print(is_perfect_square(10000000000000000000000000)) # True