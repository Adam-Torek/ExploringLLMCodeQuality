"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a','m'], ['y', 'b', 'n']]
"""

def merge(lst):
    merged_lst = []
    for sublist in lst:
        merged_lst.append([sublist[0], sublist[1]])
    return merged_lst

assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a','m'], ['y', 'b', 'n']]<|endoftext|>