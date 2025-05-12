def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # Approach 1: Sorting
    # Time complexity: O(n log n)
    # Space complexity: O(n)
    # return sorted(arr, reverse=True)[:k]

    # Approach 2: Heap
    # Time complexity: O(n log k)
    # Space complexity: O(k)
    # return heapq.nlargest(k, arr)

    # Approach 3: Quickselect
    # Time complexity: O(n)
    # Space complexity: O(1)
    # return quickselect(arr, 0, len(arr) - 1, k)

    # Approach 4: K-way merge
    # Time complexity: O(n log k)
    # Space complexity: O(k)
    # return k_way_merge(arr, k)

    # Approach 5: K-way merge with heap
    # Time complexity: O(n log k)
    # Space complexity: O(k)
    # return k_way_merge_with_heap(arr, k)

    # Approach 6: K-way merge with heap and min heap
    # Time complexity: O(n log k)
    # Space complexity: O(k)
    # return k_way_merge_with_heap_and_min_heap(arr, k)

    # Approach 7: K-way merge with heap and min heap with O(1) space
    # Time complexity: O(n log k)
    # Space complexity: O(1)
    return k_way_merge_with_heap_and_min_heap_with_O_1_space(arr, k)


def quickselect(arr, start, end, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    :param arr: List[int]
    :param start: int
    :param end: int
    :param k: int
    :return: List[int]
    """
    if start == end:
        return [arr[start]]

    pivot = arr[start]
    left = start + 1
    right = end

    while left <= right:
        if arr[left] > pivot:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        elif arr[left] < pivot:
            left += 1
        else:
            left += 1

    arr[start], arr[right] = arr[right], arr[start]

    if right == k - 1:
        return arr[:k]
    elif right < k - 1:
        return quickselect(arr, start, right - 1, k)
    else:
        return quickselect(arr, right + 1, end, k)


def k_way_merge(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    :param arr: List[int]
    :param k: int
    :return: List[int]
    """
    if k == 0:
        return []

    if k == 1: