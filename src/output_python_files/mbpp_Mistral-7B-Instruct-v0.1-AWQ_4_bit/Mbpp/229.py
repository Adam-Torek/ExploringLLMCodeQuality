"""
Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def re_arrange_array(arr, n):
    """
    Takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
    """
    # create two empty lists, one for negative and one for positive elements
    neg_list = []
    pos_list = []

    # iterate through the array and add elements to the appropriate list
    for i in range(len(arr)):
        if arr[i] < 0:
            neg_list.append(arr[i])
        else:
            pos_list.append(arr[i])

    # reverse the order of the negative list
    neg_list = neg_list[::-1]

    # concatenate the two lists and return the result
    return neg_list + pos_list[:n]

# test the function
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]