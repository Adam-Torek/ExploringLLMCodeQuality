"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(arr):
    """
    Function to find a pair with highest product from a given array of integers.
    :param arr: list of integers
    :return: tuple of two integers with highest product
    """
    n = len(arr)
    max_product = float('-inf')
    first = None
    second = None
    for i in range(n):
        for j in range(i+1, n):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                first = arr[i]
                second = arr[j]
    return (first, second)

if __name__ == "__main__":
    arr = [1,2,3,4,7,0,8,4]
    print(max_Product(arr))
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)