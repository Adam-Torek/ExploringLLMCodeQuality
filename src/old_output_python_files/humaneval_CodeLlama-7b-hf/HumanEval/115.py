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
    # TODO: Implement max_fill
    # return the number of times you need to lower the buckets
    # to empty the wells
    # grid: list of lists of ints
    # capacity: int
    # return: int
    # grid: [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # capacity: 1
    # output: 6
    # grid: [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    # capacity: 2
    # output: 5
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 5
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 1
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 2
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 3
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 4
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 5
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 6
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 7
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 8
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 9
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 10
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 11
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 12
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 13
    # output: 0
    # grid: [[0,0,0], [0,0,0]]
    # capacity: 14
    # output: 0
    #