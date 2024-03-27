"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
def find_sum(lst):
    """
    Function to find the sum of non-repeated elements in a given list.

    Parameters:
    lst (list): A list of numbers.

    Returns:
    int: The sum of non-repeated elements in the list.
    """
    # Create an empty set to store unique elements
    unique_elements = set()

    # Add all unique elements to the set
    for num in lst:
        if num not in unique_elements:
            unique_elements.add(num)

    # Convert the set back to a list and calculate the sum
    sum_of_unique_elements = sum(list(unique_elements))

    return sum_of_unique_elements</s>