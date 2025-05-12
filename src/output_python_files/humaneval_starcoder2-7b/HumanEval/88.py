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

def sort_array(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    if len(array) == 2:
        return array if array[0] < array[1] else array[::-1]
    if len(array) == 3:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 4:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 5:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 6:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 7:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 8:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 9:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 10:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 11:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 12:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 13:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 14:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 15:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 16:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 17:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 18:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 19:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 20:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len(array) == 21:
        return array if array[0] + array[-1] < array[1] + array[-2] else array[::-1]
    if len