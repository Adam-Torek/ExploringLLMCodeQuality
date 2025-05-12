"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
def comb_sort(arr):
    """
    This function sorts a list using the comb sort algorithm.
    :param arr: list of elements to be sorted
    :return: sorted list
    """
    gap = len(arr) // 2
    while gap > 0:
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
        if gap // 2 == 0:
            gap //= 10
        else:
            gap //= 2
    return arr

if __name__ == "__main__":
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    print("Test passed!")