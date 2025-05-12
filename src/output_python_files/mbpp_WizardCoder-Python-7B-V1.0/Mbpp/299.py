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

# Test the function
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
assert max_aggregate([('Alice', 80), ('Bob', 90), ('Alice', 70), ('Charlie', 85)]) == ('Alice', 150)
assert max_aggregate([('Alice', 80), ('Bob', 90), ('Charlie', 85)]) == ('Bob', 90)
assert max_aggregate([('Alice', 80), ('Bob', 90), ('Charlie', 85), ('Alice', 70)]) == ('Alice', 150)
assert max_aggregate([('Alice', 80), ('Bob', 90), ('Charlie', 85), ('Alice', 70), ('Alice', 100)]) == ('Alice', 250)
assert max_aggregate([('Alice', 80), ('Bob', 90), ('Charlie', 85), ('Alice', 70), ('Alice', 100), ('Bob', 110)]) == ('Alice', 250