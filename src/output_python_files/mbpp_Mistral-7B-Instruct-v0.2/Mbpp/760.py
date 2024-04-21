"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""
def unique_Element(numbers):
    """
    :param numbers: list of numbers
    :return: boolean value
    """
    if len(numbers) == 1:
        return True
    elif len(set(numbers)) == 1:
        return True
    else:
        return False

# Test case
assert unique_Element([1,1,1]) == True
assert unique_Element([1,2,3]) == False
assert unique_Element([1,1,2]) == False
assert unique_Element([1]) == True
assert unique_Element([]) == True</s>