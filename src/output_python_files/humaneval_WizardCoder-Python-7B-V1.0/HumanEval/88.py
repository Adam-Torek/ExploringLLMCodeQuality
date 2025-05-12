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
    if not array:
        return []
    elif len(array) == 1:
        return array
    else:
        sum_array = sum(array[0], array[-1])
        if sum_array % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)



# Test cases
print(sort_array([]))  # []
print(sort_array([5]))  # [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # [6, 5, 4, 3, 2, 1, 0]
print(sort_array([1, 2, 3, 4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(sort_array([6, 5, 4, 3, 2, 1]))  # [6, 5, 4, 3, 2, 1]
print(sort_array([1, 3, 2, 4, 5, 6]))  # [1, 3, 2, 4, 5, 6]
print(sort_array([6, 5, 4, 3, 2, 1]))  # [6, 5, 4, 3, 2, 1]
print(sort_array([1, 2, 3, 4, 5, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]
print(sort_array([7, 6, 5, 4, 3, 2, 1]))  # [7, 6, 5, 4, 3, 2, 1]
print(sort_array([1, 3, 5, 2, 4, 6]))  # [1, 3, 2, 4, 5, 6]
print(sort_array([6, 4, 2, 8, 10, 12]))  # [12, 8, 6, 4, 2]
print(sort_array([1, 3, 5, 7, 9, 11]))  # [1, 3, 5, 7, 9, 11]
print(sort_array([1, 3, 5, 7, 9, 11, 10]))  # [10, 9, 7, 5, 3, 1, 1]
print(sort_array([1, 3, 5, 7, 9, 11, 10, 8]))  # [10, 9, 7, 5, 3, 1, 1, 8]
print(sort_array([1, 3, 5, 7, 9, 11, 10, 8, 6]))  # [10, 9, 7, 5, 3, 1, 1, 8, 6]
print(sort_