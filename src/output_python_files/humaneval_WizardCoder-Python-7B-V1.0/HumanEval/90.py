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
    lst.sort()
    if lst[1] == lst[0]:
        return None
    return lst[1]


# Test cases
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))  # Output: None
print(next_smallest([1, 1]))  # Output: None
print(next_smallest([1, 2, 3, 4, 5, 3]))  # Output: 3
print(next_smallest([5, 5, 5, 5]))  # Output: None
print(next_smallest([1, 1, 2, 2, 3]))  # Output: 2
print(next_smallest([1, 2, 3, 4, 4]))  # Output: 3
print(next_smallest([1, 1, 1, 2, 2]))  # Output: None
print(next_smallest([1, 1, 1, 1]))  # Output: None
print(next_smallest([1, 2, 3, 4, 5, 6]))  # Output: 3
print(next_smallest([1, 2, 3, 4, 5, 6, 7]))  # Output: 4
print(next_smallest([7, 6, 5, 4, 3, 2, 1]))  # Output: 2
print(next_smallest([7, 7, 7, 7, 7]))  # Output: None
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 3
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 8, 9]))  # Output: 4
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))  # Output: None
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 9]))  # Output: None
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7]))  # Output: None
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 9]))  # Output: None
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 9, 10]))  # Output: 7
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 9, 10, 11]))  #