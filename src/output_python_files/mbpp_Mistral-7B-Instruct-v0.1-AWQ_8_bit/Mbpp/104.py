"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

def sort_sublists(lst):
    """
    This function takes a list of lists as input and sorts each sublist in place.
    It returns the original list.
    """
    for sublist in lst:
        sublist.sort()
    return lst