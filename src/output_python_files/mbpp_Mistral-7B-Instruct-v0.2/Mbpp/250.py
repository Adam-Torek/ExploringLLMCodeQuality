"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""
def count_X(tuple_input, element):
    count = 0
    for i in tuple_input:
        if i == element:
            count += 1
    return count

# Test case
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0</s>