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
    # Create a max heap of size k
    import heapq
    heap = []
    for i in arr[:k]:
        heapq.heappush(heap, i)

    # If the array has more elements than k, pop the smallest element from the heap
    # and add the next element from the array
    if len(arr) > k:
        for i in arr[k:]:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

    # Convert the heap to a list and return it
    return [i for i in heap]

# Test the function
arr = [-3, -4, 5]
k = 3
print(maximum(arr, k)) # [-4, -3, 5]

arr = [4, -4, 4]
k = 2
print(maximum(arr, k)) # [4, 4]

arr = [-3, 2, 1, 2, -1, -2, 1]
k = 1
print(maximum(arr, k)) # [2]