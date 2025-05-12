"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""

def re_arrange_array(arr, n):
    # Write your code here.
    if n > len(arr):
        return arr
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    neg_arr.extend(pos_arr)
    return neg_arr

print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9))
/Arrays/find_three_largest_numbers.py
"""
Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.
assert find_three_largest_numbers([1, 2, 3]) == [3, 2, 1]
assert find_three_largest_numbers([1, 2, 3, 4]) == [4, 3, 2]
assert find_three_largest_numbers([1, 2, 3, 4, 5]) == [5, 4, 3]
"""

def find_three_largest_numbers(array):
    # Write your code here.
    if len(array) < 3:
        return array
    largest_nums = [array[0], array[1], array[2]]
    for i in range(3, len(array)):
        if array[i] > largest_nums[0]:
            largest_nums[0] = array[i]
        elif array[i] > largest_nums[1]:
            largest_nums[1] = array[i]
        elif array[i] > largest_nums[2]:
            largest_nums[2] = array[i]
    return largest_nums

print(find_three_largest_numbers([1, 2, 3, 4, 5]))
/Arrays/smallest_difference.py
"""
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.
Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference.
assert smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]) == [28, 26]
"""

def smallest_difference(array1, array2):
    # Write your code here.
    array1.sort()
    array2.sort()
    smallest_diff = float('inf')
    smallest_pair = []
    for i in array1:
        for j in array2:
            diff = abs(i - j)
            if diff < smallest_diff:
                smallest_diff = diff
                smallest_pair = [i, j]
    return smallest_pair

print(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
/Arrays/two_number_sum.py
"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. If no two numbers sum up to the target sum, the function should return an empty array. Assume that the target sum always exists in the input array.
Note that the target sum must be obtained by summing two different integers in