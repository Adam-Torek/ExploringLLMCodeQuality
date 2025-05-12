"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""

def check_min_heap(arr):
    """
    :param arr: list
    :return: bool
    """
    n = len(arr)
    for i in range(n // 2, -1, -1):
        parent = i
        child = 2 * parent + 1
        if child < n and arr[child] < arr[parent]:
            return False
        child += 1
        if child < n and arr[child] < arr[parent]:
            return False
    return True

if __name__ == "__main__":
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([1, 3, 2, 4, 5, 6]) == False
    assert check_min_heap([1, 2, 3, 4, 5, 7]) == False
    assert check_min_heap([1, 2, 3, 4, 5]) == True
    assert check_min_heap([]) == True
    assert check_min_heap([1]) == True
    assert check_min_heap([1, 1]) == True
    assert check_min_heap([1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert check_min_heap([1, 1