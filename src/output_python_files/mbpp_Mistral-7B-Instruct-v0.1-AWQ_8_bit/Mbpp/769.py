"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(list1, list2):
    """
    This function takes two lists as input and returns the difference between them.
    """
    list1 = sorted(list1)
    list2 = sorted(list2)
    result = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            result.append(list1[i])
    return result


if __name__ == "__main__":
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]