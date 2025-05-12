"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""


def heap_queue_largest(numbers, n):
    """
    :param numbers: list of numbers
    :param n: number of largest integers to return
    :return: list of n largest integers
    """
    # create a min heap
    heap = []
    for number in numbers:
        heapq.heappush(heap, number)

    # pop off the top n numbers
    largest = []
    for _ in range(n):
        largest.append(heapq.heappop(heap))

    # return largest numbers in descending order
    return sorted(largest, reverse=True)


if __name__ == '__main__':
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 10))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 1))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 0))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], -1))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 100))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 1000))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 10000))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 100000))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 1000000))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 10000000))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 100000000))
    print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 1000000000))
    print(heap_queue_largest([25, 35, 22, 85, 1