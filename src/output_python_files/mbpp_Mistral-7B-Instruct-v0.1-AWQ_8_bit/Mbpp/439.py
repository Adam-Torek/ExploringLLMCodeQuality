"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""

def multiple_to_single(lst):
    """
    This function takes a list of integers and returns a single integer.
    """
    return sum(lst)

assert multiple_to_single([11, 33, 50])==113350