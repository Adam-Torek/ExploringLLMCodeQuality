"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

def frequency_lists(lst):
    freq_dict = {}
    for sublist in lst:
        for element in sublist:
            if element in freq_dict:
                freq_dict[element] += 1
            else:
                freq_dict[element] = 1
    return freq_dict

print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])) # should return {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}