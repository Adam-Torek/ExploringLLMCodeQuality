"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(lst1, lst2):
    """
    This function takes two lists as input and returns the difference between them.
    """
    # create a set of the first list
    set1 = set(lst1)

    # create a set of the second list
    set2 = set(lst2)

    # find the difference between the two sets
    diff = set1 - set2

    # convert the set to a list and return
    return list(diff)


if __name__ == "__main__":
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]