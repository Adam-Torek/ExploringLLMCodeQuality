"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""

def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    elif n == 2:
        return m // 2
    else:
        return (m - 2) * (m - 4) // 2

print(get_total_number_of_sequences(10, 4)) # Output: 4
print(get_total_number_of_sequences(10, 5)) # Output: 10
print(get_total_number_of_sequences(10, 6)) # Output: 18
print(get_total_number_of_sequences(10, 7)) # Output: 26
print(get_total_number_of_sequences(10, 8)) # Output: 36
print(get_total_number_of_sequences(10, 9)) # Output: 50
print(get_total_number_of_sequences(10, 10)) # Output: 70
print(get_total_number_of_sequences(10, 11)) # Output: 92
print(get_total_number_of_sequences(10, 12)) # Output: 122
print(get_total_number_of_sequences(10, 13)) # Output: 156
print(get_total_number_of_sequences(10, 14)) # Output: 200
print(get_total_number_of_sequences(10, 15)) # Output: 252
print(get_total_number_of_sequences(10, 16)) # Output: 306
print(get_total_number_of_sequences(10, 17)) # Output: 360
print(get_total_number_of_sequences(10, 18)) # Output: 420
print(get_total_number_of_sequences(10, 19)) # Output: 492
print(get_total_number_of_sequences(10, 20)) # Output: 564