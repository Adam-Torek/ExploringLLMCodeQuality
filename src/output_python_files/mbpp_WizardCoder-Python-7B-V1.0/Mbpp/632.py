"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""

def move_zero(lst):
    return [x for x in lst if x!=0] + [0]*lst.count(0)

#Alternate solution using two pointers
def move_zeroes(lst):
    j = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    return lst

#Test cases
print(move_zero([1,0,2,0,3,4])) # [1,2,3,4,0,0]
print(move_zero([0,0,1,2,0,3,4,0])) # [1,2,3,4,0,0,0]
print(move_zero([9,0,0,1,2,0,3,4,0])) # [9,1,2,3,4,0,0,0]
print(move_zero([1,2,3,4,5])) # [1,2,3,4,5]
print(move_zero([0,0,0,0])) # [0,0,0,0]
print(move_zero([1,2,3,4])) # [1,2,3,4]
print(move_zero([0,0,0])) # [0,0,0]
print(move_zero([1,2,0,3,4,0])) # [1,2,3,4,0,0]
print(move_zero([0,0,0,1,2,0,3,4,0])) # [1,2,3,4,0,0,0,0]
print(move_zero([0,0,1,2,0,3,4,0])) # [1,2,3,4,0,0,0]
print(move_zero([0,0,0,0,1,2,0,3,4,0])) # [1,2,3,4,0,0,0,0,0]
print(move_zero([1,2,3,4,5,6,7,8,9])) # [1,2,3,4,5,6,7,8,9]
print(move_zero([0,0,0,0,0,0,0,0,0])) # [0,0,0,0,0,0,0,0,0]
print(move_zero([0,0,0,0,0,0,0,0,1])) # [1,0,0,0,0,0,0,0,0]
print(move_zero([1,2,3,4,5,6,7,8,9])) # [1,2,3,4,5,6,7,8,9]

#Time complexity: O(n)
#Space complexity: O(1)