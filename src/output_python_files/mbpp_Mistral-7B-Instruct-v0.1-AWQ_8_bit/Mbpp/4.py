"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""

def heap_queue_largest(lst, n):
    """
    Write a function to find the n largest integers from a given list of numbers, returned in descending order.
    """
    heap = lst[:n]
    heapq.heapify(heap)
    for num in lst[n:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap


if __name__ == "__main__":
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3))