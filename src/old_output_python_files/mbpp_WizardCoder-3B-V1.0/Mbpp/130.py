"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""

def max_occurrences(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    max_freq = 0
    max_item = None
    for item in freq:
        if freq[item] > max_freq:
            max_freq = freq[item]
            max_item = item
    return max_item

# Test the function
print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])) # Output: 2<|endoftext|>