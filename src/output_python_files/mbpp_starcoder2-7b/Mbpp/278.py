"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(t):
    count = 0
    for i in t:
        if type(i) == tuple:
            break
        count += 1
    return count

assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
assert count_first_elements((1, 5, 7, (4, 6), 10, 11)) == 4
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12)) == 5
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13)) == 6
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14)) == 7
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15)) == 8
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16)) == 9
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17)) == 10
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18)) == 11
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)) == 12
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)) == 13
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)) == 14
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)) == 15
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)) == 16
assert count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,