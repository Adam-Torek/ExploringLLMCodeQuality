"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""

def Find_Max(list_of_lists):
    max_len = 0
    max_list = []
    for i in list_of_lists:
        if len(i) > max_len:
            max_len = len(i)
            max_list = i
    return max_list

assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']

"""
Write a python function to find the element of a list having minimum length.
assert Find_Min([['A'],['A','B'],['A','B','C']]) == ['A']
"""

def Find_Min(list_of_lists):
    min_len = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000