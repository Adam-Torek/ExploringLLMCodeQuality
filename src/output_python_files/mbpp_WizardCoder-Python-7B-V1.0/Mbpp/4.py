"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""
from heapq import nlargest

def heap_queue_largest(nums, n):
    return nlargest(n, nums)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3)) #[85, 75, 65]