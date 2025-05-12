"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""
def issort_list(arr):
    """
    Function to check whether a list is sorted or not.
    :param arr: list
    :return: bool
    """
    if len(arr) < 2:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
assert issort_list([1,2,4,6,8,10,12,14,16,17,1])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,1,3])==False
assert issort_list([1,2,