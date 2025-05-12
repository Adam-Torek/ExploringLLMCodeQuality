"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""

def Find_Min_Length(lst):
    min_length = len(lst[0])
    for i in lst:
        if len(i) < min_length:
            min_length = len(i)
    return min_length

print(Find_Min_Length([[1],[1,2]]) # Output: 1
print(Find_Min_Length([[1,2,3],[1,2],[1,2,3,4,5]]) # Output: 3
print(Find_Min_Length([[1,2,3,4],[1,2],[1,2,3,4,5]]) # Output: 4
print(Find_Min_Length([[1,2,3,4],[1,2],[1,2,3,4,5],[1,2,3,4,5,6,7,8]]) # Output: 4