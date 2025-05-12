"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""


def Diff(list1, list2):
    """
    :param list1: list of integers
    :param list2: list of integers
    :return: list of integers
    """
    list1.sort()
    list2.sort()
    list3 = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            list3.append(list1[i])
    return list3


if __name__ == '__main__':
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30, 40]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30, 40, 10]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30, 40, 10, 15]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30, 40, 10, 15, 20]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30, 40, 10, 15, 20, 30]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30, 40, 10, 15, 20, 30, 40]))
    print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35, 10, 15, 20, 30, 40, 10, 15, 20, 30, 40, 10]))
    print(Diff([10, 15, 20,