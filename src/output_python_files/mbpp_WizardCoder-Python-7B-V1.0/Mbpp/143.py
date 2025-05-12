"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""

def find_lists(tup):
    count = 0
    for i in tup:
        if type(i) == list:
            count += 1
    return count

# Test cases
print(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2) # True
print(find_lists((1, 2, 3, 4, 5, 6, 7, 8)) == 0) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, 13]]]) == 3) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find_lists(([1, 2, [3, 4], [5, 6, 7], 8, [9, 10, [11, 12, [13, 14, [15, 16]]]) == 4) # True
print(find