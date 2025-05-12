"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def heap_sort(lst):
    """
    This function sorts the given list using heap sort algorithm.
    """
    n = len(lst)
    heap = lst[:n//2]
    heapify(heap)
    for i in range(n//2, n):
        heap.append(lst[i])
        heapify(heap)
    return heap

def heapify(heap):
    """
    This function is used to convert the given list into heap.
    """
    n = len(heap)
    for i in range(n//2-1, 0, -1):
        if heap[i] < heap[2*i+1]:
            heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
        if heap[i] < heap[2*i+2]:
            heap[i], heap[2*i+2] = heap[2*i+2], heap[i]

if __name__ == "__main__":
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(heap_sort(lst))