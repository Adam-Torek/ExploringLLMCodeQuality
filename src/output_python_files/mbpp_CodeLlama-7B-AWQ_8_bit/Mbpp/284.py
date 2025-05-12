"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""


def check_element(list, element):
    for i in list:
        if i != element:
            return False
    return True


print(check_element(["green", "orange", "black", "white"], "blue"))