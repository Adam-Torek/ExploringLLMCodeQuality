"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
def find_first_occurrence(arr, num):
    """
    :param arr: sorted array
    :param num: number to find
    :return: index of the first occurrence of the number in the array
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    num = 5
    assert find_first_occurrence(arr, num) == 1
    print("Test passed!")</s>