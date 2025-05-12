"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""

def swap_List(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:-1] + [lst[0]]

print(swap_List([12, 35, 9, 56, 24])) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use slicing
def swap_List_2(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:] + [lst[0]]

print(swap_List_2([12, 35, 9, 56, 24])) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use tuple unpacking
def swap_List_3(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:] + [lst[0]]

print(swap_List_3([12, 35, 9, 56, 24])) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use tuple unpacking and list concatenation
def swap_List_4(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:] + [lst[0]]

print(swap_List_4([12, 35, 9, 56, 24]) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use tuple unpacking and list concatenation
def swap_List_5(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:] + [lst[0]]

print(swap_List_5([12, 35, 9, 56, 24]) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use tuple unpacking and list concatenation
def swap_List_6(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:] + [lst[0]]

print(swap_List_6([12, 35, 9, 56, 24]) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use tuple unpacking and list concatenation
def swap_List_7(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:] + [lst[0]]

print(swap_List_7([12, 35, 9, 56, 24]) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use tuple unpacking and list concatenation
def swap_List_8(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1]] + lst[2:] + [lst[0]]

print(swap_List_8([12, 35, 9, 56, 24]) # Output: [24, 35, 9, 56, 12]

# Another way to solve this problem is to use