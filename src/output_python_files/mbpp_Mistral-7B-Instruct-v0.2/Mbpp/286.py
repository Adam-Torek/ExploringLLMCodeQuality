"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    """
    :param arr: list of integers
    :param k: number of repetitions
    :param n: length of the array
    :return: largest sum of a contiguous subarray
    """
    total = sum(arr) * k
    max_sum = total
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

if __name__ == "__main__":
    arr = [10, 20, -30, -1]
    k = 4
    n = len(arr)
    print(max_sub_array_sum_repeated(arr, k, n)) # 30
    arr = [1, 2, 3, 4, 5]
    k = 2
    n = len(arr)
    print(max_sub_array_sum_repeated(arr, k, n)) # 30
    arr = [1, 2, 3, 4, 5]
    k = 3
    n = len(arr)
    print(max_sub_array_sum_repeated(arr, k, n)) # 45
    arr = [1, 2, 3, 4, 5]
    k = 1
    n = len(arr)
    print(max_sub_array_sum_repeated(arr, k, n)) # 15
    arr = [1, 2, 3, 4, 5]
    k = 5
    n = len(arr)
    print(max_sub_array_sum_repeated(arr, k, n)) # 75
    arr = [1, 2, 3, 4, 5]
    k = 0
    n = len(arr)
    print(max_sub_array_sum_repeated(arr, k, n)) # 0
    arr = [1, 2, 3, 4, 5]
    k = -1
    n = len(arr)
    print(max_sub_array_sum_repeated(arr, k, n)) # Traceback (most recent call last):
    # File "test.py", line 33, in <module>
    # print(max_sub_array_sum_repeated(arr, k, n))
    # TypeError: 'int' object is not iterable
    arr = []
    k = 1
    n = 0
    print(max_sub_array_sum_repeated(arr, k, n)) # 0
    arr = [1, 2, 3, 4, 5]
    k = 1
    n = 5
    print(max_sub_array_sum_repeated(arr, k, n)) # 30
    arr = [1, 2, 3, 4, 5]
    k = 1
    n = 1
    print(max_sub_array_sum_repeated(arr, k, n)) # 1
    arr = [1, 2, 3, 4, 5]
    k = 1
    n = 2
    print(max_sub_array_sum_repeated(arr, k, n)) # 4
    arr = [1, 2, 3, 4, 5]
    k = 1
    n = 3
    print(max_sub_array_sum_repeated(arr, k, n)) # 6
    arr = [1, 2, 3, 4, 5]
    k = 1
    n = 4
    print(max_sub_array_sum_repeated(arr, k, n)) # 10
    arr = [1, 2, 3, 4,