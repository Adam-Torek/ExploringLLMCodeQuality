"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""

def recursive_list_sum(lst):
    if isinstance(lst, list):
        return sum(lst) + recursive_list_sum(lst[1:])
    else:
        return lst

assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21<|endoftext|>