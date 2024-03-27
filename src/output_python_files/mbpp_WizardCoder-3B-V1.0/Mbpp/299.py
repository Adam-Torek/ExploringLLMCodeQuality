"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
def max_aggregate(lst):
    max_name = ''
    max_agg = 0
    for name, agg in lst:
        if agg > max_agg:
            max_name = name
            max_agg = agg
    return (max_name, max_agg)

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))<|endoftext|>