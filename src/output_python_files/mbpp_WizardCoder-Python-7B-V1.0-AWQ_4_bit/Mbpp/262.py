"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""

def split_two_parts(lst, L):
    return lst[:L], lst[L:]

# Test cases
print(split_two_parts([1,1,2,3,4,4,5,1],3)) # ([1, 1, 2], [3, 4, 4, 5, 1])
print(split_two_parts([1,2,3,4,5,6,7,8,9],4)) # ([1, 2, 3, 4], [5, 6, 7, 8, 9])
print(split_two_parts([1,2,3,4,5,6,7,8,9],10)) # ([1, 2, 3, 4, 5, 6, 7, 8, 9], [])
print(split_two_parts([1,2,3,4,5,6,7,8,9],0)) # ([], [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(split_two_parts([],3)) # ([], [])

# Edge cases
print(split_two_parts([1],1)) # ([1], [])
print(split_two_parts([],0)) # ([], [])
print(split_two_parts([1,2,3,4,5,6,7,8,9],-1) # ([], [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(split_two_parts([1,2,3,4,5,6,7,8,9],100) # ([1, 2, 3, 4, 5, 6, 7, 8, 9], [])

# Extra test cases
print(split_two_parts([1,1,2,3,4,4,5,1],0)) # ([], [1, 1, 2, 3, 4, 4, 5, 1])
print(split_two_parts([1,1,2,3,4,4,5,1],1)) # ([1], [1, 2, 3, 4, 4, 5, 1])
print(split_two_parts([1,1,2,3,4,4,5,1],2)) # ([1, 1], [2, 3, 4, 4, 5, 1])
print(split_two_parts([1,1,2,3,4,4,5,1],6)) # ([1, 1, 2, 3, 4, 4, 5, 1], [])
print(split_two_parts([1,1,2,3,4,4,5,1],7)) # ([1, 1, 2, 3, 4, 4, 5, 1], [])
print(split_two_parts([1,1,2,3,4,4,5,1],10)) # ([1, 1, 2, 3, 4, 4, 5, 1], [])
print(split_two_parts([1,1,2,3,4,4,5,1],-1) # ([], [1, 1, 2, 3, 4, 4, 5, 1])
print(split_two_parts([1,1,2,3,4,4,5,1],-2) # ([], [1, 1, 2, 3, 4, 4, 5, 1])
print(split_two_parts([1,1,2,3,4,