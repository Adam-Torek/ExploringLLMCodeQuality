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

assert left_insertion([1,2,4,5],6)==4
assert left_insertion([1,2,4,5],3)==2
assert left_insertion([1,2,4,5],1)==0
assert left_insertion([1,2,4,5],5)==4
assert left_insertion([1,2,4,5],0)==0
assert left_insertion([1,2,4,5],2)==1
assert left_insertion([1,2,4,5],4)==2
assert left_insertion([1,2,4,5],5)==4
assert left_insertion([1,2,4,5],10)==5
assert left_insertion([1,2,4,5],-1)==0
assert left_insertion([1,2,4,5],-2)==0
assert left_insertion([1,2,4,5],-3)==0
assert left_insertion([1,2,4,5],-4)==0
assert left_insertion([1,2,4,5],-5)==0
assert left_insertion([1,2,4,5],-6)==0
assert left_insertion([1,2,4,5],-7)==0
assert left_insertion([1,2,4,5],-8)==0
assert left_insertion([1,2,4,5],-9)==0
assert left_insertion([1,2,4,5],-10)==0
assert left_insertion([1,2,4,5],-11)==0
assert left_insertion([1,2,4,5],-12)==0
assert left_insertion([1,2,4,5],-13)==0
assert left_insertion([1,2,4,5],-14)==0
assert left_insertion([1,2,4,5],-15)==0
assert left_insertion([1,2,4,5],-16)==0
assert left_insertion([1,2,4,5],-17)==0
assert left_insertion([1,2,4,5],-18)==0
assert left_insertion([1,2,4,5],-19)==0
assert left_insertion([1,2,4,5],-20)==0
assert left_insertion([1,2,4,5],-21)==0
assert left_insertion([1,2,4,5],-22)==0
assert left_insertion([1,2,4,5],-23)==0
assert left_insertion([1,2,4,5],-24)==0
assert left_insertion([1,2,4,5],-25)==0
assert left_insertion([1,2,4,5],-26)==0
assert left_insertion([1,2,4,5],-27)==0
assert left_insertion([1,2,4,5],-28)==0
assert left_insertion([1,2,4,5],-29)==0
assert left_insertion([1,2,4,5],-30)==0
assert left_insertion([1,2,4,5],-31)==0
assert left_insertion([1,2,4,5],-32)==0
assert left_insertion([1,2,4,5],-33)==0
assert left_insertion([1,2,4,5],-34)==0
assert left_insertion([1,2,4,5],-35)==0
assert left_insertion([1,2,4,5],-36)==0
assert left_insertion([1,2,4,5],-37)==0
assert left_insertion([1,2,4,5],-38)==0
assert left_insertion([1,2,4,5],-39)==0
assert left_insertion([1