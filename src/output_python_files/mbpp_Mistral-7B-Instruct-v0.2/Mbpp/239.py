"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    elif m < (2 * (n - 1)):
        return 0
    else:
        return (get_total_number_of_sequences(m, n - 1) * (m - (n - 1))) // (n - 1)

assert get_total_number_of_sequences(10, 4) == 4
print(get_total_number_of_sequences(10, 5))
print(get_total_number_of_sequences(10, 6))
print(get_total_number_of_sequences(10, 7))
print(get_total_number_of_sequences(10, 8))
print(get_total_number_of_sequences(10, 9))
print(get_total_number_of_sequences(10, 10))
print(get_total_number_of_sequences(10, 11))
print(get_total_number_of_sequences(10, 12))
print(get_total_number_of_sequences(10, 13))
print(get_total_number_of_sequences(10, 14))
print(get_total_number_of_sequences(10, 15))
print(get_total_number_of_sequences(10, 16))
print(get_total_number_of_sequences(10, 17))
print(get_total_number_of_sequences(10, 18))
print(get_total_number_of_sequences(10, 19))
print(get_total_number_of_sequences(10, 20))
print(get_total_number_of_sequences(10, 21))
print(get_total_number_of_sequences(10, 22))
print(get_total_number_of_sequences(10, 23))
print(get_total_number_of_sequences(10, 24))
print(get_total_number_of_sequences(10, 25))
print(get_total_number_of_sequences(10, 26))
print(get_total_number_of_sequences(10, 27))
print(get_total_number_of_sequences(10, 28))
print(get_total_number_of_sequences(10, 29))
print(get_total_number_of_sequences(10, 30))
print(get_total_number_of_sequences(10, 31))
print(get_total_number_of_sequences(10, 32))
print(get_total_number_of_sequences(10, 33))
print(get_total_number_of_sequences(10, 34))
print(get_total_number_of_sequences(10, 35))
print(get_total_number_of_sequences(10, 36))
print(get_total_number_of_sequences(10, 37))
print(get_total_number_of_sequences(10, 38))
print(get_total_number_of_sequences(10, 39))
print(get_total_number_of_sequences(10, 40))
print(get_total_number_of_sequences(10, 41))
print(get_total_number_of_sequences(10, 42))
print(get_total_number_of_sequences