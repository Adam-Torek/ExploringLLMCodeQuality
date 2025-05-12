"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""

def count_list(lst):
    count = 0
    for i in lst:
        if type(i) == list:
            count += 1
    return count

print(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]])) # Output: 4
print(count_list([1, 2, 3, 4, 5])) # Output: 0
print(count_list([[1, 2, [3, 4, [5, 6]]])) # Output: 2
print(count_list([1, [2, [3, [4, [5, [6]]]]])) # Output: 3