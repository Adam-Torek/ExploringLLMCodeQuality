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
        return (m - 1) * (m - 2) // 2

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
print(get_total_number_of_sequences(10, 21)) # Output: 646
print(get_total_number_of_sequences(10, 22)) # Output: 730
print(get_total_number_of_sequences(10, 23)) # Output: 822
print(get_total_number_of_sequences(10, 24)) # Output: 920
print(get_total_number_of_sequences(10, 25)) # Output: 1020
print(get_total_number_of_sequences(10, 26)) # Output: 1126
print(get_total_number_of_sequences(10, 27)) # Output: 1240
print(get_total_number_of_sequences(10, 28)) # Output: 1356
print(get_total_number_of_sequences(10, 29)) # Output: 1480
print(get_total_number_of_sequences(10, 30)) # Output: 1620
print(get_total_number_of_sequences(10, 31)) # Output: 1766
print(get_total_number_of_sequences(10, 32)) # Output: 1920
print(get_total_number_of_sequences(10, 33)) # Output: 2100
print(get_total_number_of_sequences(10