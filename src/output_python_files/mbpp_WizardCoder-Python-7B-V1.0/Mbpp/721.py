"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
from typing import List

def maxAverageOfPath(matrix: List[List[int]]) -> float:
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = matrix[0][0]
    
    for i in range(1, n):
        dp[0][i] = dp[i][0] = matrix[0][i] + dp[0][i-1] + matrix[i][0] - dp[0][0]
    
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    return dp[n-1][n-1] / (n-1)

# Test cases
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]])) # 5.2
print(maxAverageOfPath([[1, 3, 1], [1, 5, 1], [4, 2, 1]])) # 3.0
print(maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 5.0
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [8, 1, 2]])) # 5.25
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [8, 1, 2], [1, 1, 1]])) # 5.25
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [8, 1, 2], [1, 1, 1], [1, 1, 1]])) # 5.25
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [8, 1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1]])) # 5.25
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [8, 1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])) # 5.25
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [8, 1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])) # 5.25
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9], [8, 1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))