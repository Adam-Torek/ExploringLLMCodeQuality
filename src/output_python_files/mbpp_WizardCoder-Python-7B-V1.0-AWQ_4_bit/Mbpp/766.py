"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""

def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

# Test cases
print(pair_wise([1,1,2,3,3,4,4,5])) #[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
print(pair_wise([1,2,3,4,5])) #[(1, 2), (2, 3), (3, 4), (4, 5)]
print(pair_wise([1])) #[(1, 1)]
print(pair_wise([])) #[]

# Time complexity: O(n)
# Space complexity: O(n)