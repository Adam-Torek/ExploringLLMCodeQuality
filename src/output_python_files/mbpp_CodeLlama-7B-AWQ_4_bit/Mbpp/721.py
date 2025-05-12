"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""


def maxAverageOfPath(matrix):
    # Write your code here
    if not matrix:
        return 0
    n = len(matrix)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = matrix[i][0]
    for j in range(n):
        dp[0][j] = matrix[0][j]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    return dp[n - 1][n - 1] / (n * n)


if __name__ == '__main__':
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(maxAverageOfPath([[1, 2, 3