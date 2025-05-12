"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(tuples):
    """
    tuples: a list of tuples
    returns: a tuple of the name and the maximum aggregate
    """
    # Your code here
    max_name = ''
    max_score = 0
    for name, score in tuples:
        if score > max_score:
            max_score = score
            max_name = name
    return (max_name, max_score)


def test_max_aggregate():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122)])==('Juan Whelan', 334)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 456)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122)])==('Juan Whelan', 588)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 710)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122)])==('Juan Whelan', 832)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 954)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',