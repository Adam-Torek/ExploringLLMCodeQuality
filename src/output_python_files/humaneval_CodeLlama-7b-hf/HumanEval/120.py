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
    # Edge case
    if not arr or k == 0:
        return []

    # Sort the array
    arr.sort()

    # Initialize the result
    result = []

    # Iterate over the array
    for i in range(k):
        result.append(arr[i])

    return result


def maximum_2(arr, k):
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
    # Edge case
    if not arr or k == 0:
        return []

    # Initialize the result
    result = []

    # Initialize the heap
    heap = []

    # Iterate over the array
    for i in range(len(arr)):
        # If the heap is not empty and the current element is greater than the
        # last element in the heap, then pop the last element from the heap
        # and append the current element to the heap
        if heap and arr[i] > heap[-1]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
        # If the heap is empty or the current element is less than the last
        # element in the heap, then append the current element to the heap
        else:
            heapq.heappush(heap, arr[i])

        # If the length of the heap is greater than k, then pop the first
        # element from the heap
        if len(heap) > k:
            heapq.heappop(heap)

    # Iterate over the heap
    for i in range(len(heap)):
        result.append(heap[i])

    return result


def maximum_3(arr, k):
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
        Output: [