"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def consecutive_duplicates(lst):
    """
    Function to remove consecutive duplicates from a given list
    :param lst: list
    :return: list
    """
    if not lst:
        return lst

    result = [lst[0]]
    for i in lst[1:]:
        if i != result[-1]:
            result.append(i)
    return result

if __name__ == "__main__":
    assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    print("Test passed")