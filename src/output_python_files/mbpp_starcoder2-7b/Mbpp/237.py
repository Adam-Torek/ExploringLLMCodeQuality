"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""

def check_occurences(list_of_tuples):
    # your code here
    return {}

# test your code
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1)]) == {(1, 3): 3, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3)]) == {(1, 3): 4, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (1, 3)]) == {(1, 3): 5, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (1, 3), (1, 3)]) == {(1, 3): 6, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (1, 3), (1, 3), (1, 3)]) == {(1, 3): 7, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3)]) == {(1, 3): 8, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3)]) == {(1, 3): 9, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3)]) == {(1, 3): 10, (2, 5): 2, (3, 6): 1}
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3), (3, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3)]) == {(1