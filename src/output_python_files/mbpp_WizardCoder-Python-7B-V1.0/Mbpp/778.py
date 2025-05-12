"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

def pack_consecutive_duplicates(lst):
    result = []
    sublist = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            sublist = [lst[i]]
            result.append(sublist)
        else:
            sublist.append(lst[i])
    return result

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
# Output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

# Test cases
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
assert pack_consecutive_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert pack_consecutive_duplicates([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [[1], [2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5, 5]
assert pack_consecutive_duplicates([1, 2, 3, 4, 5, 6]) == [[1], [2], [3], [4], [5], [6]
assert pack_consecutive_duplicates([]) == []
assert pack_consecutive_duplicates([1]) == [[1]
assert pack_consecutive_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert pack_consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1], [2], [3], [4], [5], [6], [7], [8], [9]
assert pack_consecutive_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert pack_consecutive_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7,