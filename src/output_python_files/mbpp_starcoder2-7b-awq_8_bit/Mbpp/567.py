"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""

def issort_list(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True

assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
assert issort_list([1,2,4,6,8,10,12,14,16,17,18])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20])==True
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24])==True
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27,28])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])==True
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])==False
assert issort_list([1,2,4,6,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32])==False
assert issort_list([1,2,4,6,8,10,12,14,1