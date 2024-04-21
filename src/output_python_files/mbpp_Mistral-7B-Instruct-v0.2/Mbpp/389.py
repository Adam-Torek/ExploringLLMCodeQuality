"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
def find_lucas(n):
    if n <= 0:
        return "Invalid input, n should be a positive integer"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

assert find_lucas(9) == 76
print("Test passed")</s>