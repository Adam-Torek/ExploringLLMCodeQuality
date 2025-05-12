"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""

def max_occurrences(lst):
    # create a dictionary to store the frequency of each item in the list
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    # find the item with maximum frequency
    max_freq = max(freq.values())
    max_item = [item for item, freq in freq.items() if freq == max_freq]

    # return the item with maximum frequency
    return max_item


# test the function
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2