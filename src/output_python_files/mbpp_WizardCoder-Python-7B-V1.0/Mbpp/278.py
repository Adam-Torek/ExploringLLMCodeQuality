"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            count += len(i)
        else:
            count += 1
    return count

# Test cases
print(count_first_elements((1, 5, 7, (4, 6), 10)) == 3)
print(count_first_elements((1, 5, (7, 4, 6), 10) ) == 4)
print(count_first_elements((1, 5, (7, (4, 6), 10) ) == 4)
print(count_first_elements((1, 5, (7, (4, 6, 8), 10) ) == 5)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9), 10) ) == 5)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11), 10) ) == 6)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12), 10) ) == 7)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13), 10) ) == 8)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14), 10) ) == 9)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14, 15), 10) ) == 10)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14, 15, 16), 10) ) == 11)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14, 15, 16, 17), 10) ) == 12)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14, 15, 16, 17, 18), 10) ) == 13)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19), 10) ) == 14)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), 10) ) == 15)
print(count_first_elements((1, 5, (7, (4, 6, (8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19,