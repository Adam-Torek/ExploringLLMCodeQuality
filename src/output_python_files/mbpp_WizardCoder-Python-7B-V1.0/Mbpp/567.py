"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""
def issort_list(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True

print(issort_list([1,2,4,6,8,10,12,14,16,17])) # True
print(issort_list([1,2,4,6,8,10,12,14,16,15]) # False