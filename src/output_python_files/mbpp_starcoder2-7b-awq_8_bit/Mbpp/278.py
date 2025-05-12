"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(tuple):
    count = 0
    for i in tuple:
        if type(i) == tuple:
            count += 1
    return count

assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3))) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)) == 3
assert count_first