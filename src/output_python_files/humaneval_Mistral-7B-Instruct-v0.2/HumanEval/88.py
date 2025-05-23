def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    sum_first_last = sum([array[0], array[-1]])
    if sum_first_last % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

# Testing
print(sort_array([2, 4, 3, 0, 1, 5, 6])) # [3, 5, 1, 0, 2, 6, 4]
print(sort_array([2, 4, 3, 0, 1, 5])) # [0, 1, 2, 3, 4, 5]
print(sort_array([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]
print(sort_array([1, 2, 3, 4, 5, 6])) # [5, 4, 3, 2, 1]
print(sort_array([])) # []
print(sort_array([5])) # [5]
print(sort_array([10])) # [10]
print(sort_array([10, 10])) # [10, 10]
print(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]