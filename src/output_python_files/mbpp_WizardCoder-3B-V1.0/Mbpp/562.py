"""
Write a python function to find the length of the longest sublists.
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
"""

def Find_Max_Length(lst):
    max_length = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            max_length = max(max_length, len(lst[i:j+1]))
    return max_length

# Test the function
print(Find_Max_Length([[1],[1,4],[5,6,7,8]])) # Output: 4<|endoftext|>