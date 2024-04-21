"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

def add_pairwise(lst):
    return tuple(sum(lst[i:i+2]) for i in range(0, len(lst), 2))

assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)<|endoftext|>