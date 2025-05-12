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
Write a function to find the index of the first occurrence of a value in a sorted array.
assert first_occurrence([1,2,4,5],6)==-1
assert first_occurrence([1,2,4,5],4)==2
"""
def first_occurrence(lst,val):
    if val<lst[0]:
        return -1
    if val>lst[-1]:
        return -1
    for i in range(len(lst)):
        if val==lst[i]:
            return i
    return -1

"""
Write a function to find the index of the last occurrence of a value in a sorted array.
assert last_occurrence([1,2,4,5],6)==-1
assert last_occurrence([1,2,4,5],4)==2
"""
def last_occurrence(lst,val):
    if val<lst[0]:
        return -1
    if val>lst[-1]:
        return -1
    for i in range(len(lst)-1,-1,-1):
        if val==lst[i]:
            return i
    return -1

"""
Write a function to find the index of the first occurrence of a value in a sorted array.
assert first_occurrence([1,2,4,5],6)==-1
assert first_occurrence([1,2,4,5],4)==2
"""
def first_occurrence(lst,val):
    if val<lst[0]:
        return -1
    if val>lst[-1]:
        return -1
    for i in range(len(lst)):
        if val==lst[i]:
            return i
    return -1

"""
Write a function to find the index of the last occurrence of a value in a sorted array.
assert last_occurrence([1,2,4,5],6)==-1
assert last_occurrence([1,2,4,5],4)==2
"""
def last_occurrence(lst,val):
    if val<lst[0]:
        return -1
    if val>lst[-1]:
        return -1
    for i in range(len(lst)-1,-1,-1):
        if val==lst[i]:
            return i
    return -1

"""
Write a function to find the index of the first occurrence of a value in a sorted array.
assert first_occurrence([1,2,4,5],6)==-1
assert first_occurrence([1,2,4,5],4)==2
"""
def first_occurrence(lst,val):
    if val<lst[0]:
        return -1
    if val>lst[-1]:
        return -1
    for i in range(len(lst)):
        if val==lst[i]:
            return i
    return -1

"""
Write a function to find the index of the last occurrence of a value in a sorted array.
assert last_occurrence([1,2,4,5],6)==-1
assert last_occurrence([1,2,4,5],4)==2
"""
def last_occurrence(lst,val):
    if val<lst[0]:
        return -1
    if val>lst[-1]:
        return -1
    for i in range(len(lst)-1,-1,-1):
        if val==lst[i]:
            return i
    return -1

"""
Write a function to find the index of the first occurrence of a value in a sorted array.
assert first_occurrence([1,2,4,5],6)==-1
assert first_occurrence([1,2,4,5],4)==2
"""
def first_occurrence(lst,val):
    if val<lst[0]:
        return -1
    if val>lst[-1]:
        return -1
    for i in range(len(lst)):
        if val==lst[i]:
            return i
    return -1

"""
Write a function to find the index of the last occurrence of a value in a sorted array.
assert last_occurrence([1,2,4,5],6)==-1
assert last_occurrence([1,