"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""

def merge_sorted_list(list1, list2, list3):
    """
    This function takes in three lists and returns a single sorted list.
    """
    # Combine the three lists
    combined_list = list1 + list2 + list3

    # Sort the combined list
    combined_list.sort()

    # Return the sorted list
    return combined_list


# Test the function
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]