"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""
def check_element(lst, element):
    """
    :param lst: list
    :param element: element
    :return: True if all elements in the list are equal to the given element, False otherwise
    """
    for item in lst:
        if item != element:
            return False
    return True