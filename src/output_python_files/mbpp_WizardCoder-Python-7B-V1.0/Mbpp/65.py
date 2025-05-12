"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""

def recursive_list_sum(lst):
    total = 0
    for item in lst:
        if type(item) == list:
            total += recursive_list_sum(item)
        else:
            total += item
    return total

print(recursive_list_sum([1, 2, [3,4],[5,6])) # Output: 15
print(recursive_list_sum([1, 2, [3,4, [5,6, [7,8, [9,10]]]]]) # Output: 45
print(recursive_list_sum([1, 2, [3,4, [5,6, [7,8, [9,10, [11,12, [13,14]]]]]]) # Output: 60