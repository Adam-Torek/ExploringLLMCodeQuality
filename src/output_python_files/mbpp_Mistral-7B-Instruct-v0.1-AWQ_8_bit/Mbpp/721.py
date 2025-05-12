"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""

def maxAverageOfPath(matrix):
    n = len(matrix)
    totalCost = 0
    visited = 0
    stack = [(0, 0)]
    while stack:
        x, y = stack[-1]
        visited += 1
        totalCost += matrix[x][y]
        if x < n - 1 and matrix[x + 1][y] == matrix[x][y]:
            stack.append((x + 1, y))
        elif y < n - 1 and matrix[x][y + 1] == matrix[x][y]:
            stack.append((x, y + 1))
        else:
            stack.pop()
    return totalCost / visited

matrix = [[1, 2, 3], [6, 5, 4], [7, 3, 9]]
print(maxAverageOfPath(matrix))