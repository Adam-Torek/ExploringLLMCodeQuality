"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""


def comb_sort(arr):
    """
    Sorts the list using comb sort algorithm.
    :param arr: list of elements to be sorted
    :return: sorted list
    """
    gap = len(arr)
    shrink = 1.3
    while gap > 1:
        gap = int(gap / shrink)
        for i in range(gap, len(arr)):
            if arr[i - gap] > arr[i]:
                arr[i - gap], arr[i] = arr[i], arr[i - gap]
    return arr


if __name__ == '__main__':
    print(comb_sort([5, 15, 37, 25, 79]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000, 1000000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000, 1000000, 10000000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000, 1000000, 10000000, 100000000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]))
    print(comb_sort([5, 15, 37, 25, 79, 100, 10, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 10000000000