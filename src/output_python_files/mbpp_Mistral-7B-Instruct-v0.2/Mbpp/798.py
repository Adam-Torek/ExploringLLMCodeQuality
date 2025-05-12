"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
def _sum(arr):
    """
    Function to find the sum of an array
    :param arr: list
    :return: int
    """
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    assert _sum([1, 2, 3]) == 6
    print("Test passed!")