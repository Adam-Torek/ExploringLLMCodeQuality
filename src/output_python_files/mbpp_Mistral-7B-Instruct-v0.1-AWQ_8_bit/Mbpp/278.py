"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(tuple_list):
    count = 0
    for i in range(len(tuple_list)):
        if isinstance(tuple_list[i], tuple):
            count += 1
    return count

# assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
print(count_first_elements((1, 5, 7, (4, 6), 10)))