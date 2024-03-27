"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    """
    :param m: positive integer
    :param n: positive integer
    :return: number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (m // 2) * get_total_number_of_sequences(m, n - 1)

assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(1, 1) == 1
assert get_total_number_of_sequences(5, 3) == 1
assert get_total_number_of_sequences(10, 5) == 10
assert get_total_number_of_sequences(100, 10) == 4941672740136028747778717214000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000