"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""
def division_elements(t1, t2):
    return tuple(a/b for a, b in zip(t1, t2))

# Test the function with the given example
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)<|endoftext|>