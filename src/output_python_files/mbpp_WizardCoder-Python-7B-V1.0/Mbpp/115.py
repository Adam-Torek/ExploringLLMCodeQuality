"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""
def empty_dict(lst):
    for i in lst:
        if i:
            return False
    return True

#Alternative solution
def empty_dict(lst):
    return all(not d for d in lst)

#Test cases
print(empty_dict([{},{},{}])==True) #True
print(empty_dict([{1:2},{3:4},{}])==False) #False
print(empty_dict([{},{2:3,4:5},{}]==False) #False
print(empty_dict([{1:2,3:4,5:6},{2:3,4:5}])==False) #False
print(empty_dict([{},{},{1:2}])==False) #False
print(empty_dict([{},{},{}]==True) #True
print(empty_dict([{1:2,3:4,5:6])==False) #False
print(empty_dict([{},{2:3,4:5}])==False) #False
print(empty_dict([{1:2,3:4,5:6})==False) #False
print(empty_dict([{},{2:3,4:5}])==False) #False
print(empty_dict([{},{}]==True) #True
print(empty_dict([{1:2,3:4,5:6])==False) #False
print(empty_dict([{},{2:3,4:5}])==False) #False
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{}]==True) #True
print(empty_dict([])==True) #True
print(empty_dict([{1:2,3:4,5:6])==False) #False
print(empty_dict([{2:3,4:5}])==False) #False
print(empty_dict([{1:2,3:4,5:6])==False) #False
print(empty_dict([{}]==True) #True
print(empty_dict([])==True) #True
print(empty_dict([{1:2,3:4,5:6])==False) #False
print(empty_dict([{2:3,4:5}])==False) #False
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{})==True) #True
print(empty_dict([])==True) #True
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{2:3,4:5}])==False) #False
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{})==True) #True
print(empty_dict([])==True) #True
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{2:3,4:5}])==False) #False
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{})==True) #True
print(empty_dict([])==True) #True
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{2:3,4:5}])==False) #False
print(empty_dict([{1:2,3:4,5:6)==False) #False
print(empty_dict([{})==True) #True
print(empty_dict([])==True) #True
print(empty_dict([{1:2,3:4