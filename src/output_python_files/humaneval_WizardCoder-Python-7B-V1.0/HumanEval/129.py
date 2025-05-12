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
    def dfs(grid, k, visited, path, i, j, curr_path, curr_sum, res):
        if len(path) == k:
            res.append(curr_path)
            return
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y]:
                visited[x][y] = True
                dfs(grid, k, visited, path + [grid[x][y]], x, y, curr_path + [grid[x][y]], curr_sum + grid[x][y], res)
                visited[x][y] = False

    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    res = []
    dfs(grid, k, visited, [], 0, 0, 0, [], res)
    return sorted(res[0])


# Test cases
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3)) # [1, 2, 1]
print(minPath([[5,9,3], [4,1,6], [7,8,2]], 1)) # [1]
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 2)) # [1, 2]
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 4)) # [1, 2, 3, 1]
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 5)) # [1, 2, 3, 4, 1]
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 6)) # [1, 2, 3, 4, 5, 6, 1]
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 7)) # [1, 2, 3, 4, 5, 6, 7, 8, 1]
print(minPath([[1,2,3], [4,5,6], [7,8,9]],