def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    max_element = max(arr)
    index = [0] * (max_element + 1)
    for i in range(n):
        index[arr[i]] = i
    for i in range(1, max_element + 1):
        if index[i] == 0:
            return -1
    return index[max_element]



if __name__ == "__main__":
    arr = [1, 2, 4, 3, 5]
    print(can_arrange(arr))
    arr = [1, 2, 3]
    print(can_arrange(arr))