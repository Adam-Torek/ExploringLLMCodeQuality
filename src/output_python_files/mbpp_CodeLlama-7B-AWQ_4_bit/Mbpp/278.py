"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""


def count_first_elements(t):
    count = 0
    for i in range(len(t)):
        if type(t[i]) == tuple:
            count += 1
        else:
            break
    return count


print(count_first_elements((1, 5, 7, (4, 6), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10, (1, 2, 3), 10,