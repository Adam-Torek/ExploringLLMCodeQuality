"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(t):
    result = []
    for i in range(len(t)-1):
        result.append(t[i] * t[i+1])
    return tuple(result)

print(multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)) # True
print(multiply_elements((1, 2, 3, 4, 5)) == (2, 6, 12, 20)) # True
print(multiply_elements((1, 1, 1, 1, 1)) == (1, 1, 1, 1)) # True
print(multiply_elements((1, 0, 1, 1, 1)) == (0, 0, 0, 0)) # True
print(multiply_elements((0, 1, 1, 1, 1)) == (0, 0, 0, 0)) # True
print(multiply_elements((1, 1, 0, 1, 1)) == (0, 0, 0, 0)) # True
print(multiply_elements((1, 1, 1, 0, 1)) == (0, 0, 0, 0)) # True
print(multiply_elements((1, 1, 1, 1, 0)) == (0, 0, 0, 0)) # True
print(multiply_elements((0, 0, 0, 0, 0)) == (0, 0, 0, 0)) # True
print(multiply_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == (2, 6, 24, 48, 96, 192, 324, 504, 720)) # True