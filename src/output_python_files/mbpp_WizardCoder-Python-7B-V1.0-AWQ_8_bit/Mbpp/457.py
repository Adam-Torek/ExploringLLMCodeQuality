"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""

def Find_Min(lst):
    min_length = len(lst[0])
    min_sublist = lst[0]
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
    return min_sublist

# Testing the function
print(Find_Min([[1],[1,2],[1,2,3]]) # Output: [1]
print(Find_Min([[1,2,3],[1,2],[1,2,3,4,5]]) # Output: [1,2]
print(Find_Min([[1,2,3,4],[1,2],[1,2,3,4,5]]) # Output: [1,2,3,4]
print(Find_Min([[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6,7,8,9]]) # Output: [1,2,3,4,5]
print(Find_Min([[1,2,3,4,5],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,10]]) # Output: [1,2,3,4,5,6,7,8,9]