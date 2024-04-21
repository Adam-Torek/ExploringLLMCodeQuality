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

def next_smallest(lst):
    if not lst:
        return None
    smallest = lst[0]
    second_smallest = None
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest

# Test cases
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))  # Output: None
print(next_smallest([1, 1]))  # Output: None<|endoftext|>