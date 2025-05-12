"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""

def average_tuple(t):
    return [sum(i)/len(i) for i in zip(*t)]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])==[30.5, 34.25, 27.0, 23.25]
"""

def average_list(l):
    return [sum(i)/len(i) for i in zip(*l)]

print(average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]]))


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])==[30.5, 34.25, 27.0, 23.25]
"""

def average_list(l):
    return [sum(i)/len(i) for i in zip(*l)]

print(average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]]))


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])==[30.5, 34.25, 27.0, 23.25]
"""

def average_list(l):
    return [sum(i)/len(i) for i in zip(*l)]

print(average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]]))


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])==[30.5, 34.25, 27.0, 23.25]
"""

def average_list(l):
    return [sum(i)/len(i