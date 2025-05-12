def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if len(lst) < 2:
        return None
    sorted_lst = sorted(set(lst))
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]


# Test cases
print(next_smallest([1, 2, 3, 4, 5])) # Output: 2
print(next_smallest([5, 1, 4, 3, 2])) # Output: 2
print(next_smallest([])) # Output: None
print(next_smallest([1, 1])) # Output: None
print(next_smallest([1, 2, 3, 4, 5, 3])) # Output: 3
print(next_smallest([1, 2, 3, 4, 5, 5])) # Output: 3
print(next_smallest([1, 1, 2, 2, 3])) # Output: 2
print(next_smallest([1, 2, 3, 4, 5, 5, 5])) # Output: 3
print(next_smallest([1, 1, 1, 2, 2, 3])) # Output: 2
print(next_smallest([1, 1, 1, 2, 2, 2])) # Output: None
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 3
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 6
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])) # Output: 6
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10])) # Output: 6
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11])) # Output: 6
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11])) # Output: 6
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 11])) # Output: 6
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 11, 11])) # Output: 6
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 11, 11, 11])) # Output: 6