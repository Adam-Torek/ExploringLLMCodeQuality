"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""

def frequency(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

# assert frequency([1,2,3], 4) == 0
# assert frequency([1,2,3,4,5,6,7,8,9], 4) == 1
# assert frequency([1,2,3,4,5,6,7,8,9,10], 4) == 1