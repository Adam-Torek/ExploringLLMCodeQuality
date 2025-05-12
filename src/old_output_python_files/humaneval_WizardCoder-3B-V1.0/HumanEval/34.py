def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

def merge(l1: list, l2: list):
    """Merge two sorted lists into a single sorted list
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """

def merge_sort(l: list):
    """Sort a list using merge sort algorithm
    >>> merge_sort([5, 3, 2, 1])
    [1, 2, 3, 5]
    """

def quick_sort(l: list):
    """Sort a list using quick sort algorithm
    >>> quick_sort([5, 3, 2, 1])
    [1, 2, 3, 5]
    """

def partition(l: list, low: int, high: int):
    """Partition a list around a pivot element
    >>> partition([5, 3, 2, 1], 0, 3)
    (1, 2, 3, 5)
    """

def quick_sort_partition(l: list, low: int, high: int):
    """Sort a list using quick sort algorithm and partition around a pivot element
    >>> quick_sort_partition([5, 3, 2, 1], 0, 3)
    (1, 2, 3, 5)
    """

def quick_sort_recursive(l: list, low: int, high: int):
    """Sort a list using quick sort algorithm recursively
    >>> quick_sort_recursive([5, 3, 2, 1], 0, 3)
    [1, 2, 3, 5]
    """

def quick_sort_iterative(l: list, low: int, high: int):
    """Sort a list using quick sort algorithm iteratively
    >>> quick_sort_iterative([5, 3, 2, 1], 0, 3)
    [1, 2, 3, 5]
    """

def heap_sort(l: list):
    """Sort a list using heap sort algorithm
    >>> heap_sort([5, 3, 2, 1])
    [1, 2, 3, 5]
    """

def heapify(l: list, n: int, i: int):
    """Heapify a list using heap sort algorithm
    >>> heapify([5, 3, 2, 1], 4, 0)
    [1, 2, 3, 5]
    """

def heap_sort_iterative(l: list):
    """Sort a list using heap sort algorithm iteratively
    >>> heap_sort_iterative([5, 3, 2, 1])
    [1, 2, 3, 5]
    """

def heap_sort_recursive(l: list):
    """Sort a list using heap sort algorithm recursively
    >>> heap_sort_recursive([5, 3, 2, 1])
    [1, 2, 3, 5]
    """

def heap_sort_partition(l: list, low: int, high: int):
    """Sort a list using heap sort algorithm and partition around a pivot element
    >>> heap_sort_partition([5, 3, 2, 1], 0, 3)
    (1, 2, 3, 5)
    """

def heap_sort_recursive_partition(l: list, low: int, high: int):
    """Sort a list using heap sort algorithm recursively and partition around a pivot element
    >>> heap_sort_recursive_partition([5, 3, 2, 1], 0, 3)
    (1, 2, 3, 5)
    """

def heap_sort_iterative_partition(l: list, low: int, high: int):
    """Sort a list using heap sort algorithm iteratively and partition around a pivot element
    >>> heap_sort_iterative_partition([5, 3, 2, 1], 0, 3)
    (1, 2, 3, 5)
    """

def radix_sort(l: list):
    """Sort a list using radix sort algorithm