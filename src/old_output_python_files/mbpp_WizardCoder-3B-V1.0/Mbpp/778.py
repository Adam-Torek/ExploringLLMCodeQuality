"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
def pack_consecutive_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == len(lst) - 1 or lst[i]!= lst[i+1]:
            result.append([lst[i]])
        else:
            result[-1].append(lst[i+1])
    return result

# Test the function
print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))<|endoftext|>