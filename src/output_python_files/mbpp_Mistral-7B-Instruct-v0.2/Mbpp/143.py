"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""
def find_lists(tuple_input):
    count = 0
    for i in tuple_input:
        if isinstance(i, list):
            count += 1
    return count

# Test case
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2</s>