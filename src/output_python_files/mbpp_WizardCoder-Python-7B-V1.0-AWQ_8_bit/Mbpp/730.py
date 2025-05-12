"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def consecutive_duplicates(lst):
    new_lst = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            new_lst.append(lst[i])
        else:
            continue
    return new_lst

# Testing
print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 4, 4])) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
print(consecutive_duplicates([1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(consecutive_duplicates([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(consecutive_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(consecutive_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,