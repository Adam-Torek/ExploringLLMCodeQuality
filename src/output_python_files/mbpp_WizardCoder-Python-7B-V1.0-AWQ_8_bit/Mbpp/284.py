"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""

def check_element(lst, elem):
    return all(x == elem for x in lst)

print(check_element(["green", "orange", "black", "white"],'blue')) # False
print(check_element(["green", "orange", "black", "white"],'white')) # True
print(check_element([1, 1, 1, 1],1)) # True
print(check_element([1, 2, 3, 4],1)) # False
print(check_element([],1)) # True
print(check_element([1],1)) # True
print(check_element([1,1,1,1,1,1],1)) # True
print(check_element([1,1,1,1,1,1,1],2)) # False
print(check_element([],2)) # False
print(check_element([],None)) # True
print(check_element([None,None,None],None)) # True
print(check_element([None,None,None],1)) # False
print(check_element([],"")) # True
print(check_element([""],"")) # True
print(check_element([""],"hello")) # False
print(check_element([],[])) # True
print(check_element([[],[]],[])) # False
print(check_element([[],[]],None)) # False
print(check_element([[],[]],[1,2,3])) # False
print(check_element([[],[]],[[]])) # False
print(check_element([[],[]],[[]])) # True
print(check_element([[],[]],{})) # False
print(check_element([{},{}],{})) # True
print(check_element([{},{}],[])) # False
print(check_element([{},{}],{1:2})) # False
print(check_element([{},{}],{1:2,3:4})) # False
print(check_element([{},{}],{1:2,3:4,5:6})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10,11:12})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10,11:12,13:14})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10,11:12,13:14,15:16})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10,11:12,13:14,15:16,17:18})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10,11:12,13:14,15:16,17:18,19:20})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10,11:12,13:14,15:16,17:18,19:20,21:22})) # False
print(check_element([{},{}],{1:2,3:4,5:6,7:8,9:10,11:12,13:14,15:16,17:18,19:20,21:22,23:24}))