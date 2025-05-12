"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""
def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += recursive_list_sum(i)
        else:
            total += i
    return total

assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21

# Alternative solution using list comprehension
def recursive_list_sum(lst):
    return sum(recursive_list_sum(i) if isinstance(i, list) else i for i in lst)

assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21