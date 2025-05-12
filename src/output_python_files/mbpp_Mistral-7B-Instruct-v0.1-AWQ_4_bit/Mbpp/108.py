"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""

def merge_sorted_list(list1, list2, list3):
    """
    Merges three sorted lists into one sorted list.
    """
    merged_list = []
    i = j = k = 0
    while i < len(list1) and j < len(list2) and k < len(list3):
        if list1[i] < list2[j] and list1[i] < list3[k]:
            merged_list.append(list1[i])
            i += 1
        elif list2[j] < list1[i] and list2[j] < list3[k]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list3[k])
            k += 1
    merged_list += list1[i:] + list2[j:] + list3[k:]
    return merged_list


# assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
# assert merge_sorted_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],[21, 22, 23, 24, 25, 26, 27, 28, 29, 30])==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
# assert merge_sorted_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],