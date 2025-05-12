"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(lst,val):
    if val<lst[0]:
        return 0
    if val>lst[-1]:
        return len(lst)
    for i in range(len(lst)):
        if val<lst[i]:
            return i
    return len(lst)

assert left_insertion([1,2,4,5],6)==4
assert left_insertion([1,2,4,5],3)==2
assert left_insertion([1,2,4,5],1)==0
assert left_insertion([1,2,4,5],5)==4
assert left_insertion([1,2,4,5],4)==3
assert left_insertion([1,2,4,5],2)==1
assert left_insertion([1,2,4,5],0)==0
assert left_insertion([1,2,4,5],-1)==0
assert left_insertion([1,2,4,5],10)==5
assert left_insertion([1,2,4,5],-10)==0
assert left_insertion([1,2,4,5],100)==5
assert left_insertion([1,2,4,5],-100)==0
assert left_insertion([1,2,4,5],0.5)==0
assert left_insertion([1,2,4,5],-0.5)==0
assert left_insertion([1,2,4,5],0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000