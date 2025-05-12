"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
def max_of_nth(matrix, n):
    """
    :param matrix: list of lists
    :param n: int
    :return: int
    """
    if not matrix or not matrix[0]:
        raise ValueError("Invalid matrix")
    return max(row[n] for row in matrix)

if __name__ == "__main__":
    matrix = [[5, 6, 7], [1, 3, 5], [8, 9, 19]]
    n = 2
    assert max_of_nth(matrix, n) == 19
    print("Test passed")