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

def max_fill_recursive(grid, capacity, row, col, visited, count):
    """
    Recursive solution to the max_fill problem.
    """
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0 or visited[row][col]:
        return count

    visited[row][col] = True
    count += 1

    count = max_fill_recursive(grid, capacity, row - 1, col, visited, count)
    count = max_fill_recursive(grid, capacity, row + 1, col, visited, count)
    count = max_fill_recursive(grid, capacity, row, col - 1, visited, count)
    count = max_fill_recursive(grid, capacity, row, col + 1, visited, count)

    return count

def max_fill_iterative(grid, capacity):
    """
    Iterative solution to the max_fill problem.
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and not visited[row][col]:
                count += 1
                visited[row][col] = True
                queue = [(row, col)]

                while len(queue) > 0:
                    row, col = queue.pop(0)
                    if row - 1 >= 0 and grid[row - 1][col] == 1 and not visited[row - 1][col]:
                        visited[row - 1][col] = True
                        queue.append((row - 1, col))
                    if row + 1 < len(grid) and grid[row + 1][col] == 1 and not visited[row + 1][col]:
                        visited[row + 1][col] = True
                        queue.append((row + 1, col))
                    if col - 1 >= 0 and grid[row][col - 1] == 1 and not visited[row][col - 1]:
                        visited[row][col - 1] = True
                        queue.append((row, col - 1))
                    if col + 1 < len(grid[0]) and grid[row][col + 1] == 1 and not visited[row][col + 1]:
                        visited[row][col + 1] = True
                        queue.append((row, col + 1))

    return count

def max_fill_dp(grid, capacity):
    """
    Dynamic programming solution to the max_fill problem.
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):