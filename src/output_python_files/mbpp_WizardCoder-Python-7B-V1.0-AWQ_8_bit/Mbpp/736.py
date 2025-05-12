"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, val):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left

print(left_insertion([1,2,4,5],6)) # Output: 4
print(left_insertion([1,2,4,5],3)) # Output: 2
print(left_insertion([1,2,4,5],0)) # Output: 0
print(left_insertion([1,2,4,5],10)) # Output: 4
print(left_insertion([1,2,4,5],5)) # Output: 3
print(left_insertion([1,2,4,5],4)) # Output: 2
print(left_insertion([1,2,4,5],1)) # Output: 0
print(left_insertion([1,2,4,5],2)) # Output: 1
print(left_insertion([1,2,4,5],5)) # Output: 3
print(left_insertion([1,2,4,5],4)) # Output: 2
print(left_insertion([1,2,4,5],0)) # Output: 0
print(left_insertion([1,2,4,5],10)) # Output: 4
print(left_insertion([1,2,4,5],1)) # Output: 0
print(left_insertion([1,2,4,5],2)) # Output: 1
print(left_insertion([1,2,4,5],3)) # Output: 2
print(left_insertion([1,2,4,5],0)) # Output: 0
print(left_insertion([1,2,4,5],10)) # Output: 4
print(left_insertion([1,2,4,5],1)) # Output: 0
print(left_insertion([1,2,4,5],2)) # Output: 1
print(left_insertion([1,2,4,5],3)) # Output: 2
print(left_insertion([1,2,4,5],0)) # Output: 0
print(left_insertion([1,2,4,5],10)) # Output: 4
print(left_insertion([1,2,4,5],1)) # Output: 0
print(left_insertion([1,2,4,5],2) # Output: 1
print(left_insertion([1,2,4,5],3) # Output: 2
print(left_insertion([1,2,4,5],0) # Output: 0
print(left_insertion([1,2,4,5],10) # Output: 4
print(left_insertion([1,2,4,5],1) # Output: 0
print(left_insertion([1,2,4,5],2) # Output: 1
print(left_insertion([1,2,4,5],3) # Output: 2
print(left_insertion([1,2,4,5],0) # Output: 0
print(left_insertion([1,2,4,5],10) # Output: 4
print(left_insertion([1,2,4,5],1) # Output: 0
print(left_insertion([1,2,4,5],2) # Output: 1
print(left_insertion([1,2,4,5],3) # Output: 2
print(left_insertion([1,2,4,5],0) # Output: 0
print(left_insertion([1,2,4,5],10) # Output: 4
print(