"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""

def closest_num(n):
    """
    Find the closest smaller number than n.
    """
    closest = n - 1
    while closest > n - 1:
        closest -= 1
    return closest

assert closest_num(11) == 10