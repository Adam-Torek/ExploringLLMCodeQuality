"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""


def max_sum(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])
    if len(arr) == 3:
        return max(arr[0], arr[1], arr[2])
    if len(arr) == 4:
        return max(arr[0], arr[1], arr[2], arr[3])
    if len(arr) == 5:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4])
    if len(arr) == 6:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
    if len(arr) == 7:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
    if len(arr) == 8:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7])
    if len(arr) == 9:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
    if len(arr) == 10:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9])
    if len(arr) == 11:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10])
    if len(arr) == 12:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11])
    if len(arr) == 13:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12])
    if len(arr) == 14:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13])
    if len(arr) == 15:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14])
    if len(arr) == 16:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15])
    if len(arr) == 17:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15], arr[16])