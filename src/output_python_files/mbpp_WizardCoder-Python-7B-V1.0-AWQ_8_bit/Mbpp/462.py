"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""

def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    else:
        rest = combinations_list(lst[1:])
        return rest + [[lst[0]] + c for c in rest]

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

# or

def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    else:
        rest = combinations_list(lst[1:])
        return [[lst[0]] + c for c in rest] + rest

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

# or

def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    else:
        rest = combinations_list(lst[1:])
        return [lst[0] + c for c in rest] + rest

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

# or

def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    else:
        rest = combinations_list(lst[1:])
        return [lst[0] + c for c in rest] + [c for c in rest]

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

# or

def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    else:
        rest = combinations_list(lst[1:])
        return [lst[0] + c for c in rest] + [c for c in rest] + [lst]

print(combinations_list(['orange', 'red', 'green', '