"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""
def add_pairwise(numbers):
    """
    Function to find the pairwise addition of the neighboring elements of the given tuple
    :param numbers: tuple
    :return: tuple
    """
    result = ()
    for i in range(len(numbers)-1):
        result += (numbers[i] + numbers[i+1],)
    result += (numbers[-1],)
    return result

if __name__ == "__main__":
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    print("Test passed")