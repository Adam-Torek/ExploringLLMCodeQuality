"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(lst):
    """
    This function takes a list of tuples as an input and returns the maximum aggregate value.
    """
    max_agg = 0
    for item in lst:
        if item[1] > max_agg:
            max_agg = item[1]
            max_name = item[0]
    return max_name, max_agg

# Test the function
print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))