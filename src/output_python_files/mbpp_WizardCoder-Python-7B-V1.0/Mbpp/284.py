"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""

def check_element(lst, element):
    for i in lst:
        if i != element:
            return False
    return True

print(check_element(["green", "orange", "black", "white"],'blue')) # False
print(check_element(["green", "orange", "black", "white"],'white') # True
print(check_element([1,1,1,1,1],1) # True
print(check_element([1,2,3,4,5],1) # False
print(check_element([],1) # True
print(check_element([1],1) # True
print(check_element([1,1,1,1,1,1,1],1) # True
print(check_element([1,1,1,1,1,1,1,1],2) # False
print(check_element([],2) # True
print(check_element([],"") # True
print(check_element([""],"") # True
print(check_element([""],"a") # False
print(check_element(["a","a","a","a","a","a","a"],"a") # True
print(check_element(["a","a","a","a","a","a","a"],"b") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"a") # True
print(check_element(["a","a","a","a","a","a","a"],"b") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"a") # True
print(check_element(["a","a","a","a","a","a","a"],"b") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"a") # True
print(check_element(["a","a","a","a","a","a","a"],"b") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"a") # True
print(check_element(["a","a","a","a","a","a","a"],"b") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"a") # True
print(check_element(["a","a","a","a","a","a","a"],"b") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"") # False
print(check_element(["a","a","a","a","a","a","a"],"a") # True
print(check_element(["