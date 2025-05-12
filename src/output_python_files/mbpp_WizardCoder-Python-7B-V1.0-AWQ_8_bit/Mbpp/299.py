"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(lst):
    d = {}
    for name, score in lst:
        if name in d:
            d[name] += score
        else:
            d[name] = score
    max_name = max(d, key=d.get)
    return (max_name, d[max_name])

# Test
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
assert max_aggregate([('Alice', 100), ('Bob', 80), ('Alice', 90), ('Charlie', 70), ('Bob', 95)]) == ('Alice', 190)
assert max_aggregate([('Alice', 100), ('Bob', 80), ('Charlie', 70), ('Bob', 95)]) == ('Bob', 175)
assert max_aggregate([('Alice', 100), ('Bob', 80), ('Charlie', 70)]) == ('Alice', 100)
assert max_aggregate([('Alice', 100), ('Bob', 80)]) == ('Alice', 100)
assert max_aggregate([('Alice', 100)]) == ('Alice', 100)
assert max_aggregate([]) == None