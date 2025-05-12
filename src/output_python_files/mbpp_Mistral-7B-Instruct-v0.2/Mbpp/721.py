"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
from typing import List


def max_average_of_path(matrix: List[List[int]]) -> float:
    n = len(matrix)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[-1][-1] = matrix[-1][-1]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = matrix[i][j] + dp[i + 1][j + 1] / 2

    return dp[0][0]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [6, 5, 4], [7, 3, 9]]
    print(max_average_of_path(matrix))
    assert max_average_of_path([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert max_average_of_path([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 1.0
    assert max_average_of_path([[1, 1, 1], [1, 1, 1], [1, 1, 100]]) == 3.3333333333333335
    assert max_average_of_path([[1, 1, 1], [1, 1, 1], [1, 1, 1000000]]) == 3.0
    assert max_average_of_path([[1, 1, 1], [1, 1, 1], [1, 1, 1000000000]]) == 3.0