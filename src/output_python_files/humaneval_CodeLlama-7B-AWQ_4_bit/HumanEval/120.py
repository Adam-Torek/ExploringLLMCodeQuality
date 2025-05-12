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
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    # return sorted(arr, reverse=True)[:k]

    # Approach 2: Heap
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return heapq.nlargest(k, arr)

    # Approach 3: Quickselect
    # Time complexity: O(n)
    # Space complexity: O(1)
    # return quickselect(arr, 0, len(arr) - 1, k)

    # Approach 4: Kth Largest Element
    # Time complexity: O(n)
    # Space complexity: O(1)
    # return kth_largest_element(arr, k)

    # Approach 5: Kth Largest Element with Priority Queue
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_priority_queue(arr, k)

    # Approach 6: Kth Largest Element with Max Heap
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_max_heap(arr, k)

    # Approach 7: Kth Largest Element with Min Heap
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_min_heap(arr, k)

    # Approach 8: Kth Largest Element with Priority Queue
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_priority_queue(arr, k)

    # Approach 9: Kth Largest Element with Priority Queue
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_priority_queue(arr, k)

    # Approach 10: Kth Largest Element with Priority Queue
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_priority_queue(arr, k)

    # Approach 11: Kth Largest Element with Priority Queue
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_priority_queue(arr, k)

    # Approach 12: Kth Largest Element with Priority Queue
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_priority_queue(arr, k)

    # Approach 13: Kth Largest Element with Priority Queue
    # Time complexity: O(nlogk)
    # Space complexity: O(k)
    # return kth_largest_element_with_p