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
print(check_element([1,2,3,4],1) # False
print(check_element([],1) # True
print(check_element([1],1) # True
print(check_element([1,1,1,1,1,1,1],1) # True
print(check_element([1,1,1,1,1,1,1,1],2) # False
print(check_element([],2) # False
print(check_element([2],2) # False
print(check_element([2,2,2,2,2,2,2],2) # True
print(check_element([2,2,2,2,2,2,2],3) # False
print(check_element([],3) # False
print(check_element([3],3) # False
print(check_element([3,3,3,3,3,3,3],3) # True
print(check_element([3,3,3,3,3,3,3],4) # False
print(check_element([],4) # False
print(check_element([4],4) # False
print(check_element([4,4,4,4,4,4,4],4) # True
print(check_element([4,4,4,4,4,4,4],5) # False
print(check_element([],5) # False
print(check_element([5],5) # False
print(check_element([5,5,5,5,5,5,5],5) # True
print(check_element([5,5,5,5,5,5,5],6) # False
print(check_element([],6) # False
print(check_element([6],6) # False
print(check_element([6,6,6,6,6,6,6],6) # True
print(check_element([6,6,6,6,6,6,6],7) # False
print(check_element([],7) # False
print(check_element([7],7) # False
print(check_element([7,7,7,7,7,7,7],7) # True
print(check_element([7,7,7,7,7,7,7],8) # False
print(check_element([],8) # False
print(check_element([8],8) # False
print(check_element([8,8,8,8,8,8,8],8) # True
print(check_element([8,8,8,8,8,8,8],9) # False
print(check_element([],9) # False
print(check_element([9],9) # False
print(check_element([9,9,9,9,9,9,9],9) # True
print(check_element([9,9,9,9,9,9,9],10) # False
print(check_element([],10) # False
print(check_element([10],10) # False
print(check_element([10,10,10,10,10,10,10],10) # True
print(check_element([10,10,10,10,10,10,10],11) # False
print(check_element([],11) # False
print(check_element([11],11) # False
print(check_element([11,11,11,11,11,11,11