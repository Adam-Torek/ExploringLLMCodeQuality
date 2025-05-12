"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""


def re_arrange_array(arr, n):
    # Write your code here.
    pos = []
    neg = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    return neg + pos


if __name__ == '__main__':
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 5))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 1))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 0))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 10))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 11))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 12))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 13))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 14))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 15))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 16))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 17))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 18))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 19))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 20))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 21))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 22))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 23))
    print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 24))
    print(re_arrange_array([-