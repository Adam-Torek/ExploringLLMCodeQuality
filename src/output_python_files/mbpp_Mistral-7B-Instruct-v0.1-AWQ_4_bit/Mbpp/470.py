"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

def add_pairwise(tuple_list):
    """
    This function takes a list of tuples as an input and returns a list of tuples
    where each tuple contains the sum of the neighboring elements of the given tuple.
    """
    new_list = []
    for i in range(len(tuple_list)-1):
        new_list.append((tuple_list[i][0] + tuple_list[i+1][0], tuple_list[i][1] + tuple_list[i+1][1]))
    new_list.append(tuple_list[-1])
    return new_list

# Test the function
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)