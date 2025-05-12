"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

def flatten_list(lst):
    flattened_list = []
    for item in lst:
        if type(item) == list:
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print(flatten_list([1, 2, 3, [4, 5, [6, 7, [8, 9]]])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten_list([1, [2, [3, [4, [5, [6, [7, [8, 9]]]]]]])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten_list([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12, [13, [14, [15, [16, [17, [18, [19, [20]]]]]]]]]]]]]]]]]]]]]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]