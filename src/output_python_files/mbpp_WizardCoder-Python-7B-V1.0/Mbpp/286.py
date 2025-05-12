"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    if k == 1:
        return max(arr)
    if n == 1:
        return max(arr)
    if n == 2:
        return max(arr) * k
    if n == 3:
        return max(arr) * k * 2
    if n == 4:
        return max(arr) * k * 3
    if n == 5:
        return max(arr) * k * 4
    if n == 6:
        return max(arr) * k * 5
    if n == 7:
        return max(arr) * k * 6
    if n == 8:
        return max(arr) * k * 7
    if n == 9:
        return max(arr) * k * 8
    if n == 10:
        return max(arr) * k * 9
    if n == 11:
        return max(arr) * k * 10
    if n == 12:
        return max(arr) * k * 11
    if n == 13:
        return max(arr) * k * 12
    if n == 14:
        return max(arr) * k * 13
    if n == 15:
        return max(arr) * k * 14
    if n == 16:
        return max(arr) * k * 15
    if n == 17:
        return max(arr) * k * 16
    if n == 18:
        return max(arr) * k * 17
    if n == 19:
        return max(arr) * k * 18
    if n == 20:
        return max(arr) * k * 19
    if n == 21:
        return max(arr) * k * 20
    if n == 22:
        return max(arr) * k * 21
    if n == 23:
        return max(arr) * k * 22
    if n == 24:
        return max(arr) * k * 23
    if n == 25:
        return max(arr) * k * 24
    if n == 26:
        return max(arr) * k * 25
    if n == 27:
        return max(arr) * k * 26
    if n == 28:
        return max(arr) * k * 27
    if n == 29:
        return max(arr) * k * 28
    if n == 30:
        return max(arr) * k * 29
    if n == 31:
        return max(arr) * k * 30
    if n == 32:
        return max(arr) * k * 31
    if n == 33:
        return max(arr) * k * 32
    if n == 34:
        return max(arr) * k * 33
    if n == 35:
        return max(arr) * k * 34
    if n == 36:
        return max(arr) * k * 35
    if n == 37:
        return max(arr) * k * 36
    if n == 38:
        return max(arr) * k * 37
    if n == 39:
        return max(arr) * k * 38
    if n == 40:
        return max(arr) * k * 39
    if n == 41:
        return max(arr) * k * 40
    if n == 42:
        return max(arr) * k * 41
    if n == 43:
        return max(arr) * k