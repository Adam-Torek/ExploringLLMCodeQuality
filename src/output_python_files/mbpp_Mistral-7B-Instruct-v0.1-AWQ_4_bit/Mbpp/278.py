"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(tuple_):
    count = 0
    for i in tuple_:
        if isinstance(i, tuple):
            count += 1
        else:
            count += 1
            if count > 1:
                print(f"The element {i} occurs before the tuple element.")
    return count


# assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
# assert count_first_elements((1, 5, 7, (4, 6), 10, 11)) == 4