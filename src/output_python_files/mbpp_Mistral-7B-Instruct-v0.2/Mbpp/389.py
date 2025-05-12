"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
def find_lucas(n):
    if n <= 0:
        return "Invalid input, n must be a positive integer"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(n-2):
            a, b = b, a + b
        return b

assert find_lucas(9) == 76
print(find_lucas(9))