"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""
def find_remainder(arr, n):
    """
    Function to find the product of array multiplication modulo n
    :param arr: list of integers
    :param n: integer
    :return: integer
    """
    product = 1
    for num in arr:
        product = (product * num) % n
    return product

# Test case
assert find_remainder([100, 10, 5, 25, 35, 14], 11) == 9
assert find_remainder([1, 2, 3, 4, 5], 10) == 5
assert find_remainder([1, 2, 3, 4, 5], 5) == 1
assert find_remainder([1, 2, 3, 4, 5], 2) == 1
assert find_remainder([1, 2, 3, 4, 5], 1) == 1
assert find_remainder([], 11) == 1
assert find_remainder([1], 11) == 1
assert find_remainder([1, 1], 11) == 1
assert find_remainder([1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 1
assert find_remainder([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,