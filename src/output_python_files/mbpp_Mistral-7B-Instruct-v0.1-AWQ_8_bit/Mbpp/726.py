"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(tup):
    """
    :param tup: tuple of numbers
    :return: tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}
    """
    N = len(tup)
    result = []
    for i in range(N):
        result.append(tup[i] * tup[i+1])
    return tuple(result)