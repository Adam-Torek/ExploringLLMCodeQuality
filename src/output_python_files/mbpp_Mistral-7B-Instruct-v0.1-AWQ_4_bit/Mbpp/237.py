"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""

def check_occurences(lst):
    # create an empty dictionary
    result = {}
    # iterate over the list
    for item in lst:
        # check if the item is already in the dictionary
        if item in result:
            # if it is, increment the count
            result[item] += 1
        else:
            # if it is not, add it to the dictionary with a count of 1
            result[item] = 1
    # return the dictionary
    return result