def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    n = len(grid)
    if k > n*n:
        return []
    if k == 1:
        return [min(grid[0][0])]
    if k == 2:
        return [min(grid[0][0], grid[0][1]), min(grid[1][0], grid[1][1])]

    def dfs(grid, k, i, j, visited, path, res):
        if k == 0:
            res.append(path)
            return
        visited[i][j] = True
        for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                dfs(grid, k-1, x, y, visited, path + [grid[x][y]], res)
        visited[i][j] = False

    visited = [[False for _ in range(n)] for _ in range(n)]
    res = []
    dfs(grid, k, 0, 0, visited, [grid[0][0]], res)
    return sorted(res[0])


# Test cases
grid1 = [ [1,2,3], [4,5,6], [7,8,9] ]
grid2 = [ [5,9,3], [4,1,6], [7,8,2] ]
print(minPath(grid1, 3)) # Output: [1, 2, 1]
print(minPath(grid2, 1)) # Output: [1]
print(minPath(grid2, 2)) # Output: [1, 2]
print(minPath(grid2, 3)) # Output: [1, 2, 1]
print(minPath(grid2, 4)) # Output: [1, 2, 1, 1]
print(minPath(grid2, 5)) # Output: [1, 2, 1, 2, 1]
print(minPath(grid2, 6)) # Output: [1, 2, 1, 2, 1, 1]
print(minPath(grid2, 7)) # Output: [1, 2, 1, 2, 1, 2, 1]
print(minPath(grid2, 8)) # Output: [1, 2, 1, 2,