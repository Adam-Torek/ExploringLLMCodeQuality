"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""

def recursive_list_sum(lst):
    if isinstance(lst, list):
        return sum(recursive_list_sum(x) for x in lst)
    else:
        return lst

print(recursive_list_sum([1, 2, [3, 4], [5, 6]])) # 21
print(recursive_list_sum([1, 2, [3, 4, [5, 6, [7, 8, 9], 10], 11])) # 41
print(recursive_list_sum([1, 2, [3, 4, [5, 6, [7, 8, 9], 10], 11, [12, [13, 14, [15, 16, [17, 18, 19, [20]]]]]]]) # 100