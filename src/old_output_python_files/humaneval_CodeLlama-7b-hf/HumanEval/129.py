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
    # Write your code here
    if not grid or not grid[0]:
        return []
    n = len(grid)
    m = len(grid[0])
    dp = [[[0] * k for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = grid[i][j]
    for i in range(1, k):
        for j in range(n):
            for k in range(m):
                if j > 0:
                    dp[j][k][i] = min(dp[j][k][i - 1], dp[j - 1][k][i - 1])
                if k > 0:
                    dp[j][k][i] = min(dp[j][k][i - 1], dp[j][k - 1][i - 1])
    return dp[n - 1][m - 1][k - 1]


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    print(minPath(grid, k))
    grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
    k = 1
    print(minPath(grid, k))
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 2
    print(minPath(grid, k))
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    print(minPath(grid, k))
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 4
    print(minPath(grid, k))
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 5
    print(minPath(grid, k))
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 6
    print(min