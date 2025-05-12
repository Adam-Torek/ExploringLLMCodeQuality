"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""

def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = matrix[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[n-1][n-1] / (n-1)

# Test cases
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]])) # 5.2
print(maxAverageOfPath([[1, 3, 1], [1, 5, 3], [4, 2, 1]])) # 3.0
print(maxAverageOfPath([[1, 2], [3, 4]])) # 2.5
print(maxAverageOfPath([[1, 3, 5, 9], [2, 8, 3, 7], [5, 6, 4, 1], [6, 9, 8, 2]])) # 5.0
print(maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 5.0
print(maxAverageOfPath([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) # 7.5
print(maxAverageOfPath([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])) # 8.0
print(maxAverageOfPath([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])) # 10.0
print(maxAverageOfPath([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]])) # 12.0
print(maxAverageOfPath([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11,