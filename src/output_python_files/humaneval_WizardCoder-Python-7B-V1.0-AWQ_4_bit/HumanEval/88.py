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

    first_last_sum = array[0] + array[-1]
    if first_last_sum % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)



def test_sort_array():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_array([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_array([1, 3, 5, 2, 4]) == [1, 3, 2, 4, 5]
    assert sort_array([1, 3, 5, 2, 4, 6]) == [6, 5, 4, 3, 2, 1]
    assert sort_array([1, 3, 5, 2, 4, 6, 7]) == [1, 3, 2, 4, 5, 6, 7]
    assert sort_array([1, 3, 5, 2, 4, 6, 7, 8]) == [8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_array([1, 3, 5, 2, 4, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_array([1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_array([1, 3, 5, 2, 4, 6, 7, 8, 9, 10, 11]) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_array([1, 3, 5, 2, 4, 6, 7, 8, 9, 10, 11, 12]) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_array([1, 3, 5, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13]) == [1