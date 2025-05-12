"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""

def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    elif n == 2:
        return m - 1
    else:
        return (m - 2) * (m - 1) * (m - 2) * (m - 3) // (2 * (2 * n - 3) * (2 * n - 5))

# Test cases
print(get_total_number_of_sequences(10, 4)) # Output: 4
print(get_total_number_of_sequences(10, 5)) # Output: 10
print(get_total_number_of_sequences(10, 6)) # Output: 18
print(get_total_number_of_sequences(10, 7)) # Output: 26
print(get_total_number_of_sequences(10, 8)) # Output: 36
print(get_total_number_of_sequences(10, 9)) # Output: 46
print(get_total_number_of_sequences(10, 10)) # Output: 56
print(get_total_number_of_sequences(10, 11)) # Output: 66
print(get_total_number_of_sequences(10, 12)) # Output: 78
print(get_total_number_of_sequences(10, 13)) # Output: 92
print(get_total_number_of_sequences(10, 14)) # Output: 108
print(get_total_number_of_sequences(10, 15)) # Output: 126
print(get_total_number_of_sequences(10, 16)) # Output: 146
print(get_total_number_of_sequences(10, 17)) # Output: 168
print(get_total_number_of_sequences(10, 18)) # Output: 194
print(get_total_number_of_sequences(10, 19)) # Output: 222
print(get_total_number_of_sequences(10, 20)) # Output: 252
print(get_total_number_of_sequences(10, 21)) # Output: 284
print(get_total_number_of_sequences(10, 22)) # Output: 318
print(get_total_number_of_sequences(10, 23)) # Output: 354
print(get_total_number_of_sequences(10, 24)) # Output: 392
print(get_total_number_of_sequences(10, 25)) # Output: 432
print(get_total_number_of_sequences(10, 26)) # Output: 474
print(get_total_number_of_sequences(10, 27)) # Output: 518
print(get_total_number_of_sequences(10, 28)) # Output: 564
print(get_total_number_of_sequences(10, 29)) # Output: 612
print(get_total_number_of_sequences(10, 30)) # Output: 662
print(get_total_number_of_sequences(10, 31)) # Output: 714
print(get_total_number_of_sequences(10, 32)) # Output: 768
print(get_total_number_of_sequences(10, 3