"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""
def check_element(lst, element):
    """
    :param lst: list
    :param element: element
    :return: boolean
    """
    return all(i == element for i in lst)

assert check_element(["green", "orange", "black", "white"],'blue')==False
assert check_element(["green", "orange", "black", "white"],'green')==True