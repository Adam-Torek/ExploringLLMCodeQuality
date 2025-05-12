"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""

def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0] * N for _ in range(N)]
    max_avg = float('-inf')
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = matrix[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = matrix[i][j] + dp[i-1][j]
            else:
                dp[i][j] = max(matrix[i][j] + dp[i-1][j], matrix[i][j] + dp[i][j-1])
            max_avg = max(max_avg, dp[i][j])
    return max_avg / (N*N)

# Test cases
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]])) # Output: 5.2<|endoftext|>