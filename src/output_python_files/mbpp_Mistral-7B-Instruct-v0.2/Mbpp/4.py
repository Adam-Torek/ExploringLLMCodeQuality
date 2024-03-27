"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""
import heapq

def heap_queue_largest(numbers, n):
    """
    :param numbers: list of numbers
    :param n: number of largest numbers to return
    :return: list of n largest numbers
    """
    return heapq.nlargest(n, numbers)

if __name__ == "__main__":
    numbers = [25, 35, 22, 85, 14, 65, 75, 22, 58]
    n = 3
    assert heap_queue_largest(numbers, n) == [85, 75, 65]
    print("Test passed")</s>