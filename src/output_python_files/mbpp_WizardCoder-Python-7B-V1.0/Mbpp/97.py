"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
from typing import List, Dict

def frequency_lists(lst: List[List[int]) -> Dict[int, int]:
    freq_dict = {}
    for sublist in lst:
        for num in sublist:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
    return freq_dict

# Test cases
print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])) # should return {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
print(frequency_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # should return {1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
print(frequency_lists([[1, 2, 3, 2, 3, 2, 3, 4, 5, 6, 2, 7, 8, 9, 5])) # should return {1: 1, 2: 3, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
print(frequency_lists([[1, 2, 3, 4, 5, 6, 7, 8, 9])) # should return {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
print(frequency_lists([])) # should return {}
print(frequency_lists([[1, 1, 1, 1, 1, 1, 1])) # should return {1: 5}
print(frequency_lists([[1, 2, 3, 4, 5, 6, 7, 8, 9])) # should return {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
print(frequency_lists([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # should return {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
print(frequency_lists([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])) # should return {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 2}
print(frequency_lists([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10