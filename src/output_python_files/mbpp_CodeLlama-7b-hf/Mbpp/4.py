"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""


def heap_queue_largest(nums, n):
    """
    :param nums: list of numbers
    :param n: number of largest integers to return
    :return: list of n largest integers
    """
    if n > len(nums):
        raise ValueError("n must be less than or equal to the length of nums")
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if not isinstance(nums, list):
        raise TypeError("nums must be a list")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    # create a min heap
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    # pop off the top n elements
    largest = []
    for _ in range(n):
        largest.append(heapq.heappop(heap))

    # return largest in descending order
    return sorted(largest, reverse=True)


if __name__ == "__main__":
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 4))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 6))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 7))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 8))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 9))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 10))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 11))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 12))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 13))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 14))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 15))
    print(heap_queue_largest([25, 3