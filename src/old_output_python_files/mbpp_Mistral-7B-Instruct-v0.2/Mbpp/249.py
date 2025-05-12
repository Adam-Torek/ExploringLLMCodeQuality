"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""
def intersection_array(arr1, arr2):
    """
    :param arr1: list
    :param arr2: list
    :return: list
    """
    result = []
    for i in arr1:
        if i in arr2 and i not in result:
            result.append(i)
    return result

if __name__ == "__main__":
    arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
    arr2 = [1, 2, 4, 8, 9]
    assert intersection_array(arr1, arr2) == [1, 2, 8, 9]
    print("Test passed")