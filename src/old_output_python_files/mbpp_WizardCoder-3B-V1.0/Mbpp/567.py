"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""
def issort_list(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

# Test cases
print(issort_list([1,2,4,6,8,10,12,14,16,17])) # True
print(issort_list([1,2,3,4,5])) # True
print(issort_list([1,2,3,4,5,6])) # False
print(issort_list([1,2,3,4,5,6,7])) # False<|endoftext|>