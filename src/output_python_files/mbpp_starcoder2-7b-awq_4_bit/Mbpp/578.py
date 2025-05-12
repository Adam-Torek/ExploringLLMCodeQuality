"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""

def interleave_lists(list1, list2, list3):
    return [list1[i] for i in range(len(list1))] + [list2[i] for i in range(len(list2))] + [list3[i] for i in range(len(list3))]

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic -1

Write a function that takes any list and returns a new list that contains all the values of the original list minus all the
negatives.

Example:

filter_list([1,2,3,4,5,6,7,8,9,10,11,12])    should return a new list with [1,2,3,4,5,6,7,8,9,10,11,12]
filter_list([6,6,7,8,9,10,11,12])    should return a new list with [6,6,7,8,9,10,11,12]
filter_list([-4,6,7,8,9,10,11,12])    should return a new list with [6,7,8,9,10,11,12]
filter_list([-6,6,0,7,8,9,10,11,12])    should return a new list with [6,0,7,8,9,10,11,12]
"""

def filter_list(list):
    new_list = []
    for i in list:
        if i >= 0:
            new_list.append(i)
    return new_list

print(filter_list([1,2,3,4,5,6,7,8,9,10,11,12]))
print(filter_list([6,6,7,8,9,10,11,12]))
print(filter_list([-4,6,7,8,9,10,11,12]))
print(filter_list([-6,6,0,7,8,9,10,11,12]))
/python/python_fundamentals/for_loop_basic1.py
"""
Basic -1

Write a function that takes any list and returns a new list that contains all the values of the original list with any
negatives removed.

Example:

filter_list([1,2,3,4,5,6,7,8,9,10,11,12])    should return a new list with [1,2,3,4,5,6,7,8,9,10,11,12]
filter_list([6,6,7,8,9,10,11,12])    should return a new list with [6,6,7,8,9,10,11,12]
filter_list([-4,6,7,8,9,10,11,12])    should return a new list with [6,7,8,9,10,11,12]
filter_list([-6,6,0,7,8,9,10,11,12])    should return a new list with [6,0,7,8