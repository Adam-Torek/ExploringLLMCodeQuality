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
        raise ValueError("Matrix cannot be empty")

    max_num = matrix[0][n]
    for row in matrix:
        if row[n] > max_num:
            max_num = row[n]

    return max_num

if __name__ == "__main__":
    matrix = [[5, 6, 7], [1, 3, 5], [8, 9, 19]]
    n = 2
    assert max_of_nth(matrix, n) == 19

    matrix = [[], [1, 2], [3, 4], [5, 6]]
    n = 1
    assert max_of_nth(matrix, n) == 6

    matrix = [[], [1], [2], [3]]
    n = 0
    assert max_of_nth(matrix, n) == 2

    matrix = [[], [], []]
    n = 0
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = 1
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = 3
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = 4
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = -1
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = 5
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = "a"
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = 1.5
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = 1 + 1j
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = 0.5
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = complex(0, 1)
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = set()
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = frozenset()
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = list()
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = tuple()
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = dict()
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = str()
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = bool()
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = range(10)
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = bytearray(b"abc")
    assert max_of_nth(matrix, n) is None

    matrix = [[], [], []]
    n = bytearray(b"\x00\