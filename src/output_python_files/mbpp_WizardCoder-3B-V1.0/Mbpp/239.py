"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""

def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    elif n == 2:
        return m * (m - 1) // 2
    else:
        return get_total_number_of_sequences(m, n - 1) + get_total_number_of_sequences(m, n - 2)

# Test cases
assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(10, 5) == 10
assert get_total_number_of_sequences(10, 6) == 20
assert get_total_number_of_sequences(10, 7) == 42
assert get_total_number_of_sequences(10, 8) == 88<|endoftext|>