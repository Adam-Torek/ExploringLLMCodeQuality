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
    def lower_bucket(grid, bucket_capacity, row, col, direction):
        """
        Helper function to lower the bucket in the given direction
        """
        if direction == 'left':
            col -= 1
        elif direction == 'right':
            col += 1
        elif direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1

        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
            grid[row][col] = 0
            bucket_capacity -= 1
            if bucket_capacity == 0:
                return grid, bucket_capacity, True
            else:
                return lower_bucket(grid, bucket_capacity, row, col, direction)
        else:
            return grid, bucket_capacity, False

    def count_lowers(grid, bucket_capacity):
        """
        Helper function to count the number of times the bucket needs to be lowered
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid, bucket_capacity, can_lower = lower_bucket(grid, bucket_capacity, i, j, 'left')
                    if can_lower:
                        count += 1
                        grid, bucket_capacity, can_lower = lower_bucket(grid, bucket_capacity, i, j, 'right')
                        if can_lower:
                            count += 1
                        else:
                            return count
                    else:
                        return count
                    grid, bucket_capacity, can_lower = lower_bucket(grid, bucket_capacity, i, j, 'up')
                    if can_lower:
                        count += 1
                        grid, bucket_capacity, can_lower = lower_bucket(grid, bucket_capacity, i, j, 'down')
                        if can_lower:
                            count += 1
                        else:
                            return count
                        return count

    def count_lowers_helper(grid, bucket_capacity):
        """
        Helper function to count the number of times the bucket needs to be lowered
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    grid[i][j] = 0
                    bucket_capacity -= 1
                    if bucket_capacity == 0:
                        return count
                    count += count_lowers