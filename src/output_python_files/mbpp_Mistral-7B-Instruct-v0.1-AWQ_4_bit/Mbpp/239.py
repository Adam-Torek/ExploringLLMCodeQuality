"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""

def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    else:
        return sum([get_total_number_of_sequences(m, n-1) for i in range(2, m+1)])


assert get_total_number_of_sequences(10, 4) == 4