"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(lst, n):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j] and lst[i] != n and lst[j] != n:
                count += 1
    return count


# Test cases
print(count_Pairs([1,2,1],3))
print(count_Pairs([1,2,3,4],3))
print(count_Pairs([1,2,3,4,5],3))