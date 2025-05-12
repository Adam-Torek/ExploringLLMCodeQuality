"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""
def right_insertion(lst,val):
    if val<lst[0]:
        return 0
    if val>lst[-1]:
        return len(lst)
    for i in range(len(lst)):
        if val<lst[i]:
            return i
    return len(lst)

"""
Write a function to find the maximum value in a list of integers.
assert max_value([1,2,3,4,5])==5
"""
def max_value(lst):
    max_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max_val:
            max_val=lst[i]
    return max_val

"""
Write a function to find the minimum value in a list of integers.
assert min_value([1,2,3,4,5])==1
"""
def min_value(lst):
    min_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min_val:
            min_val=lst[i]
    return min_val

"""
Write a function to find the maximum value in a list of integers.
assert max_value([1,2,3,4,5])==5
"""
def max_value(lst):
    max_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max_val:
            max_val=lst[i]
    return max_val

"""
Write a function to find the minimum value in a list of integers.
assert min_value([1,2,3,4,5])==1
"""
def min_value(lst):
    min_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min_val:
            min_val=lst[i]
    return min_val

"""
Write a function to find the maximum value in a list of integers.
assert max_value([1,2,3,4,5])==5
"""
def max_value(lst):
    max_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max_val:
            max_val=lst[i]
    return max_val

"""
Write a function to find the minimum value in a list of integers.
assert min_value([1,2,3,4,5])==1
"""
def min_value(lst):
    min_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min_val:
            min_val=lst[i]
    return min_val

"""
Write a function to find the maximum value in a list of integers.
assert max_value([1,2,3,4,5])==5
"""
def max_value(lst):
    max_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max_val:
            max_val=lst[i]
    return max_val

"""
Write a function to find the minimum value in a list of integers.
assert min_value([1,2,3,4,5])==1
"""
def min_value(lst):
    min_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min_val:
            min_val=lst[i]
    return min_val

"""
Write a function to find the maximum value in a list of integers.
assert max_value([1,2,3,4,5])==5
"""
def max_value(lst):
    max_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max_val:
            max_val=lst[i]
    return max_val

"""
Write a function to find the minimum value in a list of integers.
assert min_value([1,2,3,4,5])==1
"""
def min_value(lst):
    min_val=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min_val:
            min_val=lst[i]
    return min_val

"""