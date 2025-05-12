"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""

def maxAverageOfPath(matrix):
    n = len(matrix)
    visited = [[False for j in range(n)] for i in range(n)]
    visited[0][0] = True
    visited[n-1][n-1] = True
    totalCost = 0
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if not visited[i][j] and matrix[i][j] > 0:
                visited[i][j] = True
                totalCost += matrix[i][j]
                count += 1
    return totalCost / count

matrix = [[1, 2, 3], [6, 5, 4], [7, 3, 9]]
print(maxAverageOfPath(matrix))