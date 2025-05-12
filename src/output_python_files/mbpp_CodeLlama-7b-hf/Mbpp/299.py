"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(tuples):
    """
    tuples: a list of tuples
    returns: a tuple (name, score)
    """
    # Your code here
    max_score = 0
    max_name = ''
    for name, score in tuples:
        if score > max_score:
            max_score = score
            max_name = name
    return (max_name, max_score)


def test_max_aggregate():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122)])==('Juan Whelan', 244)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 244)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122)])==('Juan Whelan', 366)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 366)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122)])==('Juan Whelan', 498)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 498)
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84),('Juan Whelan',1