"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
def count_first_elements(tuple_):
    count = 0
    for i in tuple_:
        if isinstance(i, tuple):
            count += len(tuple_[:tuple.index(i)])
        else:
            count += 1
    return count

assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3</s>