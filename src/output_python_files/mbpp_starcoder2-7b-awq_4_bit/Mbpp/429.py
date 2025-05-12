"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""

def and_tuples(tup1, tup2):
    return (tup1[0] & tup2[0], tup1[1] & tup2[1], tup1[2] & tup2[2], tup1[3] & tup2[3])

assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)

"""
Write a function to extract the elementwise or tuples from the given two tuples.
assert or_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (10, 6, 6, 9)
"""

def or_tuples(tup1, tup2):
    return (tup1[0] | tup2[0], tup1[1] | tup2[1], tup1[2] | tup2[2], tup1[3] | tup2[3])

assert or_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (10, 6, 6, 9)

"""
Write a function to extract the elementwise xor tuples from the given two tuples.
assert xor_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (10, 6, 4, 6)
"""

def xor_tuples(tup1, tup2):
    return (tup1[0] ^ tup2[0], tup1[1] ^ tup2[1], tup1[2] ^ tup2[2], tup1[3] ^ tup2[3])

assert xor_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (10, 6, 4, 6)

"""
Write a function to extract the elementwise not tuples from the given two tuples.
assert not_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (~10, ~4, ~6, ~9)
"""

def not_tuples(tup1, tup2):
    return (~tup1[0], ~tup1[1], ~tup1[2], ~tup1[3])

assert not_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (~10, ~4, ~6, ~9)

"""
Write a function to extract the elementwise left shift tuples from the given two tuples.
assert left_shift_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (10 << 5, 4 << 2, 6 << 3, 9 << 3)
"""

def left_shift_tuples(tup1, tup2):
    return (tup1[0] << tup2[0], tup1[1] << tup2[1], tup1[2] << tup2[2], tup1[3] << tup2[3])

assert left_shift_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (10 << 5, 4 << 2, 6 << 3, 9 << 3)

"""
Write a function to extract the elementwise right shift tuples from the given two tuples.
assert right_shift_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (10 >> 5, 4 >> 2, 6 >> 3, 9 >> 3)
"""

def right_shift_tuples(tup1, tup2):
    return (tup1[0] >> tup2[0], tup1[1] >> tup2[1], tup1[2] >> tup2[2], tup1[3] >> tup2[3])

assert right_shift_tuples((10, 4, 6,