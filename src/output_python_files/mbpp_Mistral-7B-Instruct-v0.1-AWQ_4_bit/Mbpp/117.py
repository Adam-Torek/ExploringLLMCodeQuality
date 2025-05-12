"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(lst):
    """
    Converts all possible convertible elements in a list of lists to floats.
    """
    new_lst = []
    for sublist in lst:
        new_sublist = []
        for item in sublist:
            if isinstance(item, str):
                try:
                    new_item = float(item)
                except ValueError:
                    new_item = item
                new_sublist.append(new_item)
        new_lst.append(new_sublist)
    return new_lst