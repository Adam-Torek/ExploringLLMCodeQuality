"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, val):
    for i in range(len(arr)):
        if arr[i] > val:
            return i
    return len(arr)

print(left_insertion([1,2,4,5],6)) # 4
print(left_insertion([1,2,4,5],3)) # 2
print(left_insertion([1,2,4,5],0)) # 0
print(left_insertion([1,2,4,5],7)) # 4
print(left_insertion([1,2,4,5],5)) # 4
print(left_insertion([1,2,4,5],4)) # 3
print(left_insertion([1,2,4,5],1)) # 0
print(left_insertion([1,2,4,5],2)) # 1
print(left_insertion([1,2,4,5],5)) # 4
print(left_insertion([1,2,4,5],4)) # 3
print(left_insertion([1,2,4,5],0)) # 0
print(left_insertion([1,2,4,5],1)) # 0
print(left_insertion([1,2,4,5],2)) # 1
print(left_insertion([1,2,4,5],3)) # 2
print(left_insertion([1,2,4,5],6)) # 4
print(left_insertion([1,2,4,5],7)) # 4
print(left_insertion([1,2,4,5],0)) # 0
print(left_insertion([1,2,4,5],1)) # 0
print(left_insertion([1,2,4,5],2)) # 1
print(left_insertion([1,2,4,5],3)) # 2
print(left_insertion([1,2,4,5],4)) # 3
print(left_insertion([1,2,4,5],5)) # 4
print(left_insertion([1,2,4,5],6)) # 4
print(left_insertion([1,2,4,5],7)) # 4
print(left_insertion([1,2,4,5],0)) # 0
print(left_insertion([1,2,4,5],1)) # 0
print(left_insertion([1,2,4,5],2)) # 1
print(left_insertion([1,2,4,5],3)) # 2
print(left_insertion([1,2,4,5],4)) # 3
print(left_insertion([1,2,4,5],5)) # 4
print(left_insertion([1,2,4,5],6)) # 4
print(left_insertion([1,2,4,5],7)) # 4
print(left_insertion([1,2,4,5],0)) # 0
print(left_insertion([1,2,4,5],1)) # 0
print(left_insertion([1,2,4,5],2)) # 1
print(left_insertion([1,2,4,5],3)) # 2
print(left_insertion([1,2,4,5],4)) # 3
print(left_insertion([1,2,4,5],5)) # 4
print(left_insertion([1,2,4,5],6)) # 4
print(left_insertion([1,2,4,5],7)) # 4
print(left_insertion([1,2,4,5],0)) # 0
print(left_insertion([1,2,4,5],1)) # 0