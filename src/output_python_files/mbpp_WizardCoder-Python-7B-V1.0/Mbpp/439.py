"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""

def multiple_to_single(lst):
    return int("".join(str(num) for num in lst))

print(multiple_to_single([11, 33, 50])) # Output: 113350