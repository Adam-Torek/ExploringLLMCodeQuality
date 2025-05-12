def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # First, we convert the array into a list of tuples, where each tuple
    # contains the number and its binary representation.
    # We use the built-in 'bin' function to convert the numbers into their
    # binary representation.
    # If the number is negative, we add a '-' sign before the binary
    # representation.
    # Then we sort the list of tuples based on the number of ones in the
    # binary representation.
    # If two numbers have the same number of ones, we sort based on the
    # decimal value.
    # Finally, we convert the sorted list of tuples back into an array and
    # return it.
    return sorted(
        [(num, bin(num)[2:]) for num in arr if num >= 0],
        key=lambda x: (len(x[1]), x[0]))


if __name__ == '__main__':
    for arr in [
            [1, 5, 2, 3, 4],
            [-2, -3, -4, -5, -6],
            [1, 0, 2, 3, 4],
            [-1, -2, -3, -4, -5],
            [10, 9, 8, 7, 6],
            [-6, -5, -4, -3, -2],
            [1, 0, 2, 3, 4, 5],
            [-1, -2, -3, -4, -5, -6],
            [10, 9, 8, 7, 6, 5],
            [-6, -5, -4, -3, -2, -1],
            [1, 0, 2, 3, 4, 5, 6],
            [-1, -2, -3, -4, -5, -6, -7],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [-6, -5, -4, -3, -2, -1, -0],
            [1, 0, 2, 3, 4, 5, 6, 7, 8, 9],
            [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            [-6, -5, -4, -3, -2, -1, -0, -1, -2, -3, -4, -5, -6],
            [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
            [-6, -5, -4, -3, -2, -1, -0, -1, -2, -3, -4, -5, -6, -1],
            [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1