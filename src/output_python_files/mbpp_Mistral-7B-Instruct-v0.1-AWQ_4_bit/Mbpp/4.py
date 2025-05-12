"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""

def heap_queue_largest(numbers, n):
    """
    Write a function to find the n largest integers from a given list of numbers, returned in descending order.
    """
    if n > len(numbers):
        return []
    else:
        return sorted(numbers, reverse=True)[:n]


# assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))