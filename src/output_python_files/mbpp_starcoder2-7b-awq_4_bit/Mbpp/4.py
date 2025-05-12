"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""

def heap_queue_largest(lst, n):
    """
    :param lst: list of numbers
    :param n: number of largest elements to return
    :return: list of n largest elements in descending order
    """
    # TODO: Write your code here
    heapq.heapify(lst)
    return heapq.nlargest(n, lst)

def test_heap_queue_largest():
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 1) == [85]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 0) == []
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 10) == [85, 75, 65, 58, 35, 25, 22, 22, 14]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 2) == [85, 75]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5) == [85, 75, 65, 58, 35]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 6) == [85, 75, 65, 58, 35, 25]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 7) == [85, 75, 65, 58, 35, 25, 22]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 8) == [85, 75, 65, 58, 35, 25, 22, 22]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 9) == [85, 75, 65, 58, 35, 25, 22, 22, 14]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 11) == [85, 75, 65, 58, 35, 25, 22, 22, 14]
    assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 12) == [85, 75, 65, 58, 35, 25, 22, 22, 14]
    assert heap_queue_largest([25, 3