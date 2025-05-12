"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(tuple_of_numbers):
    """
    This function takes as input a tuple of numbers and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
    """
    result = []
    for i in range(len(tuple_of_numbers)):
        result.append(tuple_of_numbers[i] * tuple_of_numbers[i+1])
    return tuple(result)

# assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
# assert multiply_elements((2, 3, 4)) == (6, 12, 24)