"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""


def merge_sorted_list(list1, list2, list3):
    """
    :param list1: list of integers
    :param list2: list of integers
    :param list3: list of integers
    :return: list of integers
    """
    result = []
    i = 0
    j = 0
    k = 0
    while i < len(list1) and j < len(list2) and k < len(list3):
        if list1[i] < list2[j] < list3[k]:
            result.append(list1[i])
            i += 1
        elif list1[i] > list2[j] > list3[k]:
            result.append(list3[k])
            k += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    while k < len(list3):
        result.append(list3[k])
        k += 1
    return result


if __name__ == '__main__':
    print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110], [19, 20, 11, 56, 25, 233, 154], [24, 26, 54, 48]))
    print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110], [19, 20, 11, 56, 25, 233, 154], [24, 26, 54, 48, 100]))
    print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110], [19, 20, 11, 56, 25, 233, 154], [24, 26, 54, 48, 100, 101]))
    print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110], [19, 20, 11, 56, 25, 233, 154], [24, 26, 54, 48, 100, 101, 102]))
    print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110], [19, 20, 11, 56, 25, 233, 154], [24, 26, 54, 48, 100, 101, 102, 103]))
    print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110], [19, 20, 11, 56, 25, 233, 154], [24, 26, 54, 48, 100,