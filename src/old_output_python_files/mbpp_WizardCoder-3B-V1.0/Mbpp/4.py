"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""

def heap_queue_largest(numbers, n):
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)
    return heap

# Test the function
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]<|endoftext|>