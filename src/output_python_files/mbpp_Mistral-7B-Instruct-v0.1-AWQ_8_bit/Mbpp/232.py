"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""

def larg_nnum(lst, n):
    """
    Returns a list containing the n largest items from the list.
    """
    # sort the list in descending order
    lst.sort(reverse=True)
    # return the first n items of the sorted list
    return lst[:n]

# test the function
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])