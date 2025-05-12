"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            count += 1
    return count

# Test the function
assert count_Pairs([1,2,1],3) == 2<|endoftext|>