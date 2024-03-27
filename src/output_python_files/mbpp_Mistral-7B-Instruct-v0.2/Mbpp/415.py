"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(arr):
    """
    :param arr: list of integers
    :return: tuple of two integers with highest product
    """
    if len(arr) < 2:
        raise ValueError("Array should have at least 2 elements")

    max_product = arr[0] * arr[1]
    first = arr[0]
    second = None

    for num in arr[1:]:
        if num * first > max_product:
            second = max_product[0]
            max_product = (num, num * first)
        elif num * second is not None and num * second > max_product:
            max_product = (num, num * second)

    return max_product

if __name__ == "__main__":
    assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
    assert max_Product([-1, -2, 3, 4, 7, 0, 8, 4]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, -4]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, None]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1, 2, 3, 4, 7, 0, 8, "four"]) == (7, 8)
    assert max_Product([1,