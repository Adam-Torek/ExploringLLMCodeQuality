"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n


# assert not is_perfect_square(10)
# assert is_perfect_square(16)
# assert is_perfect_square(25)