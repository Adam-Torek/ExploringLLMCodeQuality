"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""


def get_Inv_Count(arr):
    """
    :param arr: list of integers
    :return: number of inversions
    """
    if len(arr) <= 1:
        return 0
    else:
        mid = len(arr) // 2
        left = get_Inv_Count(arr[:mid])
        right = get_Inv_Count(arr[mid:])
        inv_count = 0
        i = 0
        j = 0
        k = 0
        while i < len(arr) and j < len(arr):
            if arr[i] <= arr[j]:
                arr[k] = arr[i]
                i += 1
            else:
                arr[k] = arr[j]
                inv_count += (mid - i)
                j += 1
            k += 1
        while i < len(arr):
            arr[k] = arr[i]
            i += 1
            k += 1
        while j < len(arr):
            arr[k] = arr[j]
            j += 1
            k += 1
        return left + right + inv_count


if __name__ == '__main__':
    print(get_Inv_Count([1, 20, 6, 4, 5]))
    print(get_Inv_Count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(get_Inv_Count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(get_Inv_Count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))
    print(get_Inv_Count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 3