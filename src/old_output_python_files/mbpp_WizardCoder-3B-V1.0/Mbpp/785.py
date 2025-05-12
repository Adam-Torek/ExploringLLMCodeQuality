"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(s):
    return tuple(map(int, s.strip("()").split(",")))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)<|endoftext|>