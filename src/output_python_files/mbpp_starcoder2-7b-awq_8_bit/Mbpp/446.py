"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""

def count_Occurrence(tuple, list):
    count = 0
    for i in list:
        count += tuple.count(i)
    return count

assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r'] ) == 3
assert count_Occurrence(('a', 'a', 'c', 'b', '