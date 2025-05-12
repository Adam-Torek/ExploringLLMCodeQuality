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
    def count_buckets(grid, capacity):
        n = len(grid)
        m = len(grid[0])
        buckets = 0
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buckets += 1
        while buckets > 0:
            count += 1
            new_buckets = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        if i > 0 and grid[i-1][j] == 0:
                            grid[i-1][j] = 1
                            new_buckets += 1
                        if i < n-1 and grid[i+1][j] == 0:
                            grid[i+1][j] = 1
                            new_buckets += 1
                        if j > 0 and grid[i][j-1] == 0:
                            grid[i][j-1] = 1
                            new_buckets += 1
                        if j < m-1 and grid[i][j+1] == 0:
                            grid[i][j+1] = 1
                            new_buckets += 1
            buckets = new_buckets
            buckets = min(buckets, capacity)
        return count

    def count_water(grid, capacity):
        n = len(grid)
        m = len(grid[0])
        water = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    water += 1
        return water

    def count_lowers(grid, capacity):
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += math.ceil(count_water(grid, capacity) / capacity)
                    for k in range(n):
                        for l in range(m):
                            grid[k][l] = 0
        return count

    return count_lowers(grid, capacity)

# Test cases
print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) # 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)) # 5
print(max_fill