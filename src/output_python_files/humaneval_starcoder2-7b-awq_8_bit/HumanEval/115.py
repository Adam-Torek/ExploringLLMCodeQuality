import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """

def max_fill_recursive(grid, capacity, row, col, visited):
    """
    Recursive solution to the max_fill problem.
    """
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0
    if grid[row][col] == 0:
        return 0
    if visited[row][col]:
        return 0
    visited[row][col] = True
    return 1 + max_fill_recursive(grid, capacity, row - 1, col, visited) + \
        max_fill_recursive(grid, capacity, row + 1, col, visited) + \
        max_fill_recursive(grid, capacity, row, col - 1, visited) + \
        max_fill_recursive(grid, capacity, row, col + 1, visited)

def max_fill_iterative(grid, capacity):
    """
    Iterative solution to the max_fill problem.
    """
    if not grid:
        return 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    max_fill = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and not visited[row][col]:
                max_fill += max_fill_recursive(grid, capacity, row, col, visited)
    return max_fill

def max_fill_dp(grid, capacity):
    """
    Dynamic programming solution to the max_fill problem.
    """
    if not grid:
        return 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    max_fill = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and not visited[row][col]:
                max_fill += max_fill_recursive(grid, capacity, row, col, visited)
    return max_fill

def max_fill_dp_space_optimized(grid, capacity):
    """
    Dynamic programming solution to the max_fill problem.
    """
    if not grid:
        return 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    max_fill = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and not visited[row][col]:
                max_fill += max_fill_recursive(grid, capacity, row, col, visited)
    return max_fill

def max_fill_dp_space_optimized_2(grid, capacity):
    """
    Dynamic programming solution to the max_fill problem.
    """
    if not grid:
        return 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    max_fill = 0
    for row in range(len(grid)):
        for col in range(len(grid[0]))