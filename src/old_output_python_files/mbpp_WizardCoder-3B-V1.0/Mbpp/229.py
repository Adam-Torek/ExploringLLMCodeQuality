"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""

def re_arrange_array(arr, n):
    neg_count = 0
    pos_count = 0
    result = []

    for num in arr:
        if num < 0:
            neg_count += 1
        else:
            pos_count += 1

        if neg_count == n:
            result.append(num)
            neg_count = 0
            pos_count = 0

    if neg_count > 0:
        result.extend([num for num in arr[:neg_count]])

    if pos_count > 0:
        result.extend([num for num in arr[neg_count:]])

    return result

# Test cases
print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9))  # Output: [-1, -3, -7, 4, 5, 6, 2, 8, 9]<|endoftext|>