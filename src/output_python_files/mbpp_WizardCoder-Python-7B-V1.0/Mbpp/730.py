"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def consecutive_duplicates(lst):
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    return result

# Test cases
print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
print(consecutive_duplicates([1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
print(consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(consecutive_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # [1]
print(consecutive_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4])) # [1, 2, 3, 4]
print(consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(consecutive_duplicates([])) # []
print(consecutive_duplicates([1])) # [1]
print(consecutive_duplicates([1, 1])) # [1]
print(consecutive_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # [1]
print(consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(consecutive_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) # [1, 2, 3]
print(consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]