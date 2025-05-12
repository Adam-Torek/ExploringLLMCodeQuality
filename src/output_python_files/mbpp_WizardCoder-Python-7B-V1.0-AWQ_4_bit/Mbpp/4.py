"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""

import heapq

def heap_queue_largest(nums, n):
    """
    Returns the n largest integers from a given list of numbers, in descending order.
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3)) #[85, 75, 65]