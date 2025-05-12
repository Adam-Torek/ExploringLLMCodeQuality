"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""

def is_Sub_Array(list1,list2):
    for i in range(len(list1)):
        if list1[i] == list2[0]:
            if list1[i:i+len(list2)] == list2:
                return True
    return False

print(is_Sub_Array([1,4,3,5],[1,2]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5,1,4,3,5]))
print(is_Sub_Array([1,4,3,5],[1,4,3,5,