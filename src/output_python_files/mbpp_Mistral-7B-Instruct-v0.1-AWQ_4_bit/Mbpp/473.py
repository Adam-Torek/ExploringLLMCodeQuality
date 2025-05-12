"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""

def tuple_intersection(tuple_list, tuple_set):
    intersection = []
    for tuple in tuple_list:
        for item in tuple_set:
            if tuple == item:
                intersection.append(item)
    return intersection

# Driver code  
tuple_list = [(3, 4), (5, 6), (9, 10), (4, 5)]
tuple_set = [(5, 4), (3, 4), (6, 5), (9, 11)]

print(tuple_intersection(tuple_list, tuple_set))