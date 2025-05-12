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
        dp[i][i] = matrix[i][i]
    for i in range(n - 1):
        dp[i][i + 1] = matrix[i][i] + matrix[i + 1][i + 1]
    for i in range(n - 2):
        dp[i][i + 2] = matrix[i][i] + matrix[i + 1][i + 1] + matrix[i + 2][i + 2]
    for i in range(n - 3, -1, -1):
        for j in range(i + 3, n):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j], dp[i + 2][j]) + matrix[i][j]
    return dp[0][n - 1] / (n * n)


if __name__ == "__main__":
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [10, 11, 12]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [10, 11, 12], [13, 14, 15]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27]]))
    print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18],