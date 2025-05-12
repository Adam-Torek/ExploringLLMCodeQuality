"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def comb_sort(lst):
    """
    This function sorts a list of elements using the comb sort algorithm.
    """
    n = len(lst)
    if n <= 1:
        return lst

    # Divide the list into two halves
    mid = n // 2
    left = lst[:mid]
    right = lst[mid:]

    # Recursively sort the two halves
    left = comb_sort(left)
    right = comb_sort(right)

    # Combine the two sorted halves
    return combine(left, right)


def combine(left, right):
    """
    This function combines two sorted lists into one sorted list.
    """
    result = []
    i = j = 0

    # Compare and combine elements from the two lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left list
    result.extend(left[i:])

    # Add any remaining elements from the right list
    result.extend(right[j:])

    return result