"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""

def and_tuples(t1, t2):
    return (t1[0] & t2[0], t1[1] & t2[1], t1[2] & t2[2], t1[3] & t2[3])

assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)<|endoftext|>