"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""

def merge(lst):
    return [[lst[i][0] for i in range(len(lst))], [lst[i][1] for i in range(len(lst))]]

print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]) # True
print(merge([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]) # True
print(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]) # True