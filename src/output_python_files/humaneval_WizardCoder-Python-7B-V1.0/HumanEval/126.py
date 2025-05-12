def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            return False
    return True

# Test cases
print(is_sorted([5])) # True
print(is_sorted([1, 2, 3, 4, 5])) # True
print(is_sorted([1, 3, 2, 4, 5])) # False
print(is_sorted([1, 2, 3, 4, 5, 6])) # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7])) # True
print(is_sorted([1, 2, 2, 3, 3, 4])) # True
print(is_sorted([1, 2, 2, 2, 3, 4])) # False
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 7, 8, 9])) # False
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # True
print(is_sorted([1, 2, 3, 4,