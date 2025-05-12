"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""


def check_element(list, element):
    for item in list:
        if item != element:
            return False
    return True


print(check_element(["green", "orange", "black", "white"], "blue"))
print(check_element(["green", "orange", "black", "white"], "white"))
print(check_element(["green", "orange", "black", "white"], "green"))
print(check_element(["green", "orange", "black", "white"], "black"))
print(check_element(["green", "orange", "black", "white"], "orange"))
print(check_element(["green", "orange", "black", "white"], "red"))
print(check_element(["green", "orange", "black", "white"], "yellow"))
print(check_element(["green", "orange", "black", "white"], "purple"))
print(check_element(["green", "orange", "black", "white"], "pink"))
print(check_element(["green", "orange", "black", "white"], "brown"))
print(check_element(["green", "orange", "black", "white"], "gray"))
print(check_element(["green", "orange", "black", "white"], "blue"))
print(check_element(["green", "orange", "black", "white"], "yellow"))
print(check_element(["green", "orange", "black", "white"], "purple"))
print(check_element(["green", "orange", "black", "white"], "pink"))
print(check_element(["green", "orange", "black", "white"], "brown"))
print(check_element(["green", "orange", "black", "white"], "gray"))
print(check_element(["green", "orange", "black", "white"], "blue"))
print(check_element(["green", "orange", "black", "white"], "yellow"))
print(check_element(["green", "orange", "black", "white"], "purple"))
print(check_element(["green", "orange", "black", "white"], "pink"))
print(check_element(["green", "orange", "black", "white"], "brown"))
print(check_element(["green", "orange", "black", "white"], "gray"))
print(check_element(["green", "orange", "black", "white"], "blue"))
print(check_element(["green", "orange", "black", "white"], "yellow"))
print(check_element(["green", "orange", "black", "white"], "purple"))
print(check_element(["green", "orange", "black", "white"], "pink"))
print(check_element(["green", "orange", "black", "white"], "brown"))
print(check_element(["green", "orange", "black", "white"], "gray"))
print(check_element(["green", "orange", "black", "white"], "blue"))
print(check_element(["green", "orange", "black", "white"], "yellow"))
print(check_element(["green", "orange", "black", "white"], "purple"))
print(check_element(["green", "orange", "black", "white"], "pink"))
print(check_element(["green", "orange", "black", "white"], "brown"))
print(check_element(["green", "orange", "black", "white"], "gray"))
print(check_element(["green", "orange", "black", "white"], "blue"))
print(check_element(["green", "orange", "black", "white"], "yellow"))
print(check_element(["green", "orange", "black", "white"], "purple"))
print(check_element(["green", "orange", "black", "white"], "pink"))