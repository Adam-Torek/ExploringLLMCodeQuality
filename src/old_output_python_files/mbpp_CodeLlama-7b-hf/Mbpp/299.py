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
    name = ''
    score = 0
    for i in tuples:
        if i[1] > score:
            name = i[0]
            score = i[1]
    return (name, score)


print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))


"""
Write a function to calculate the minimum aggregate from the list of tuples.
assert min_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Peter Nichols', 7)
"""

def min_aggregate(tuples):
    """
    tuples: a list of tuples
    returns: a tuple (name, score)
    """
    # Your code here
    name = ''
    score = 0
    for i in tuples:
        if i[1] < score:
            name = i[0]
            score = i[1]
    return (name, score)


print(min_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))


"""
Write a function to calculate the average aggregate from the list of tuples.
assert average_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==(103.25)
"""

def average_aggregate(tuples):
    """
    tuples: a list of tuples
    returns: a float
    """
    # Your code here
    total = 0
    for i in tuples:
        total += i[1]
    return total/len(tuples)


print(average_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))


"""
Write a function to calculate the median aggregate from the list of tuples.
assert median_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==(94.0)
"""

def median_aggregate(tuples):
    """
    tuples: a list of tuples
    returns: a float
    """
    # Your code here
    total = 0
    for i in tuples:
        total += i[1]
    return total/len(tuples)


print(median_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))


"""
Write a function to calculate the mode aggregate from the list of tuples.
assert mode_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 2)
"""

def mode