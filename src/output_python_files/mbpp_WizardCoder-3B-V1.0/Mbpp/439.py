"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""
def multiple_to_single(lst):
    return int(''.join(map(str, lst)))

# Test the function
assert multiple_to_single([11, 33, 50])==113350<|endoftext|>