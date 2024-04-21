"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count