"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    """
    :param arr: list of integers
    :param x: integer
    :return: integer
    """
    if x not in arr:
        return -1
    else:
        return arr.index(x) + arr[::-1].index(x)

print(last([1,2,3],1)) # Output: 0
print(last([1,2,3,4,4,4,4,5],4) # Output: 4
print(last([1,2,3,4,5],6) # Output: -1