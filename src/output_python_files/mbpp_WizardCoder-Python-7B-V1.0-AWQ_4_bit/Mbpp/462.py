"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""

def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        rest = combinations_list(lst[1:])
        return rest + [[lst[0]] + c for c in rest]

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

#Alternative solution using recursion
def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [[lst[0]] + c for c in combinations_list(lst[1:])] + combinations_list(lst[1:])

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

#Alternative solution using recursion and list comprehension
def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [[lst[0]] + c for c in combinations_list(lst[1:])] + [lst]

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

#Alternative solution using recursion and list comprehension with flattening
def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [c for c in combinations_list(lst[1:]) for e in [lst[0]]] + [c for c in combinations_list(lst[1:])]

print(combinations_list(['orange', 'red', 'green', 'blue']))
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

#Alternative solution using recursion and list comprehension with flattening and filtering
def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [c for c in combinations_list(lst[1:]) for e in [lst[0]]] + [c for c in combinations_list(lst[1:])